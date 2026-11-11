"""Render a truthful current-stargazer cohort chart, not historical net totals."""
import argparse
import datetime as dt
import json
import math
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
import urllib.error

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
UTC = dt.timezone.utc


def timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(UTC)


def request(route, token, body=None):
    command = ['gh', 'api', '--hostname', 'github.com', route,
               '-H', 'Accept: application/vnd.github.star+json',
               '-H', 'X-GitHub-Api-Version: 2022-11-28']
    if body is not None:
        command += ['--input', '-']
    for attempt in range(3):
        response = subprocess.run(command, input=None if body is None else json.dumps(body),
                                  capture_output=True, text=True, timeout=45,
                                  env={**os.environ, 'GH_TOKEN': token})
        if response.returncode == 0:
            return json.loads(response.stdout)
        match = re.search(r'HTTP (\d{3})', response.stderr)
        code = int(match.group(1)) if match else 503
        if code in (401, 403, 404, 429) or attempt == 2:
            # Do not log response bodies, account details or authentication data.
            raise urllib.error.HTTPError(route, code, 'GitHub API request failed', {}, None)
        time.sleep(2 ** attempt)


def fetch_times(repo, token):
    try:
        result = []
        for page in range(1, 501):
            rows = request(f'repos/{repo}/stargazers?per_page=100&page={page}', token)
            if not isinstance(rows, list):
                raise ValueError('Unexpected stargazer response')
            result.extend(row['starred_at'] for row in rows)
            if len(rows) < 100:
                return result, 'REST stargazers'
        raise ValueError('Pagination limit reached; refusing partial data')
    except urllib.error.HTTPError as error:
        if error.code not in (403, 404):
            raise
    owner, name = repo.split('/')
    result, cursor = [], None
    query = '''query($owner:String!,$name:String!,$cursor:String){
      repository(owner:$owner,name:$name){stargazers(first:100,after:$cursor){
        edges{starredAt} pageInfo{hasNextPage endCursor}
      }}
    }'''
    for _ in range(500):
        response = request('graphql', token, {'query': query, 'variables': {
            'owner': owner, 'name': name, 'cursor': cursor}})
        if response.get('errors'):
            raise ValueError('GitHub denied the star timeline; keeping the last good chart')
        stars = response['data']['repository']['stargazers']
        result.extend(row['starredAt'] for row in stars['edges'])
        if not stars['pageInfo']['hasNextPage']:
            return result, 'GraphQL stargazers'
        next_cursor = stars['pageInfo']['endCursor']
        if not next_cursor or next_cursor == cursor:
            raise ValueError('Invalid pagination cursor')
        cursor = next_cursor
    raise ValueError('Pagination limit reached; refusing partial data')


def fetch(repo, token):
    for _ in range(3):
        before = request(f'repos/{repo}', token)
        times, source = fetch_times(repo, token)
        after = request(f'repos/{repo}', token)
        if before['stargazers_count'] == after['stargazers_count'] == len(times):
            now = dt.datetime.now(UTC)
            parsed = sorted(timestamp(value) for value in times)
            if any(value < timestamp(after['created_at']) or value > now for value in parsed):
                raise ValueError('Invalid star timestamp')
            return {'repository': repo, 'created_at': after['created_at'],
                    'as_of': now.isoformat(), 'current_stars': len(times),
                    'starred_at': [value.isoformat() for value in parsed],
                    'source': source,
                    'semantics': 'Current stargazers by original star date; removed stars excluded. Not historical net totals.',
                    'timezone': 'UTC'}
    raise ValueError('Star count changed while fetching; keeping the last good chart')


def points(snapshot):
    start, end = timestamp(snapshot['created_at']), timestamp(snapshot['as_of'])
    if end < start or snapshot['current_stars'] != len(snapshot['starred_at']):
        raise ValueError('Invalid snapshot bounds or count')
    events = sorted(timestamp(value) for value in snapshot['starred_at'])
    if any(value < start or value > end for value in events):
        raise ValueError('Event outside chart bounds')
    # Exact step holds: never invent growth between observations.
    result = [(start, 0)]
    for count, event in enumerate(events, 1):
        result.extend([(event, count - 1), (event, count)])
    result.append((end, len(events)))
    return result


def smooth_points(snapshot):
    """Monotone visual interpolation through real event totals; never overshoot."""
    exact = points(snapshot)  # Validate before producing any visual output.
    nodes = {exact[0][0]: 0}
    for date, count in exact[1:]:
        nodes[date] = count  # Combine simultaneous events at their true timestamp.
    nodes = sorted(nodes.items())
    result = [nodes[0]]
    for (start, low), (end, high) in zip(nodes, nodes[1:]):
        for index in range(1, 65):
            t = index / 64
            # Cubic Bezier with horizontal endpoint tangents: C1 continuous,
            # passes through every observation, bounded and non-decreasing.
            value = low + (high - low) * (3*t*t - 2*t*t*t)
            result.append((start + (end-start)*t, value))
    return result


def month_ticks(start, end):
    """Calendar-month ticks, thinned evenly for long-running projects."""
    month = start.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    months = []
    while month <= end:
        months.append(month)
        month = month.replace(year=month.year+1, month=1) if month.month == 12 else month.replace(month=month.month+1)
    if len(months) > 7:
        months = [months[round(index*(len(months)-1)/6)] for index in range(7)]
    return months


def render(snapshot, output):
    width, height = 1800, 660
    im = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(im)
    def font(size):
        return ImageFont.truetype(str(ROOT / 'Handlee-Regular.ttf'), size)
    def text(x, y, value, size=24, fill='#30343b', anchor=None):
        draw.text((x, y), value, font=font(size), fill=fill, anchor=anchor)
    art = Image.open(ROOT / 'anjing-growth.png').convert('RGBA')
    art.thumbnail((370, 445), Image.Resampling.LANCZOS)
    im.paste(art, (20, 145), art)
    text(445, 12, 'Growing Together', 66)
    text(445, 87, snapshot['repository'], 25, '#616771')
    text(1735, 33, f"{snapshot['current_stars']} Stars", 39, '#258bd0', 'ra')
    text(445, 124, 'Every Star, a Little Encouragement', 24, '#616771')
    x0, x1, y0, y1 = 460, 1715, 220, 510
    data = points(snapshot)
    start, end = data[0][0], data[-1][0]
    # Begin the axis at the calendar month; no data is invented before creation.
    start = start.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    duration = max((end - start).total_seconds(), 1)
    step = max(1, math.ceil(max(1, snapshot['current_stars']) / 4))
    ceiling = max(step, math.ceil(snapshot['current_stars'] / step) * step)
    def xy(item):
        date, count = item
        return (x0 + (date - start).total_seconds() / duration * (x1 - x0),
                y1 - count / ceiling * (y1 - y0))
    for tick in range(0, ceiling + 1, step):
        y = y1 - tick / ceiling * (y1 - y0)
        draw.line((x0, y, x1, y), fill='#edf0f2', width=2)
        text(x0 - 18, y, str(tick), 25, '#555b64', 'rm')
    draw.line((x0, y0 - 6, x0, y1, x1 + 8, y1), fill='#4b5058', width=3)
    text(x0 - 45, y0 - 45, 'Stars', 26)
    coords = [xy(item) for item in smooth_points(snapshot)]
    # Same exact vertices for both strokes: texture must not alter values.
    draw.line(coords, fill='#7cc6f0', width=7)
    draw.line(coords, fill='#258bd0', width=3)
    for date in sorted(set(timestamp(value) for value in snapshot['starred_at'])):
        count = sum(timestamp(value) <= date for value in snapshot['starred_at'])
        x, y = xy((date, count))
        draw.ellipse((x-4, y-4, x+4, y+4), fill='#258bd0')
    latest_x, latest_y = coords[-1]
    draw.ellipse((latest_x-7, latest_y-7, latest_x+7, latest_y+7), fill='#e8b72b')
    dates = month_ticks(start, end)
    for index, value in enumerate(dates):
        x, _ = xy((value, 0))
        draw.line((x, y1, x, y1+8), fill='#4b5058', width=2)
        label = value.strftime('%b %Y')
        text(x, y1+15, label, 29, '#555b64', 'la' if index == 0 else 'ra' if x > x1-90 else 'ma')
    text(1735, 565, 'Month (UTC)', 22, '#555b64', 'ra')
    text(445, 584, 'Current stargazers by original star date; removed stars excluded.', 22, '#666c74')
    text(445, 617, 'Dots: real data; curve: smoothed guide. Updated ' + end.strftime('%Y-%m-%d %H:%M UTC'), 21, '#666c74')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Prepare both outputs before replacing; API failures never overwrite existing assets.
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        png, raw = Path(temp)/'chart.png', Path(temp)/'chart.json'
        im.save(png, optimize=True)
        raw.write_text(json.dumps({**snapshot, 'visualization':
            'Dots are actual event totals; the monotone smoothed curve is visual interpolation, not observed intermediate counts.'}, indent=2) + '\n')
        os.replace(png, output)
        os.replace(raw, output.with_suffix('.json'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', required=True)
    parser.add_argument('--output', default='assets/star-growth.png')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repository):
        raise ValueError('Invalid repository name')
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token:
        token = subprocess.check_output(['gh', 'auth', 'token'], text=True).strip()
    snapshot = fetch(args.repository, token)
    render(snapshot, args.output)
    print(f"Rendered {args.repository}: {snapshot['current_stars']} current stars; {snapshot['source']}")


if __name__ == '__main__':
    main()
