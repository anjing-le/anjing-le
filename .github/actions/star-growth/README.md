# Anjing Star Growth

The illustration is decorative. Every chart vertex, tick, date and total is rendered from GitHub data, never ImageGen.

The cohort chart reconstructs the original star dates of **current stargazers**. It excludes removed stars and is **not a historical net-total series**. This limitation is printed on every image. The zero baseline is repository creation, timestamps and labels use UTC, and step holds never interpolate fictional growth. Small counts retain integer axes. Empty data stays flat at zero.

REST star timestamps are used first, with GraphQL fallback for repository Actions tokens. Pagination is bounded; the total is checked against repository metadata before/after fetching. Incomplete, unauthorized or changing responses fail without overwriting the last good chart. Only timestamps and aggregate counts are saved; no usernames, IDs or credentials enter published artifacts.

Each repository updates its own assets using its built-in GITHUB_TOKEN. No PAT or third-party chart service is needed when the workflow token can read its own timeline. Workflows run once daily and may also be dispatched manually. GitHub image caching means a README may not immediately display the newest image.

Artwork: generated with built-in imagegen; see artwork.prompt.md. Font: Handlee from google/fonts, under SIL OFL, bundled with its unchanged license. Pillow is pinned to 11.3.0. Application builds, releases and OTA are unrelated to this chart. The renderer also requires GitHub CLI (preinstalled on GitHub-hosted Ubuntu runners).
