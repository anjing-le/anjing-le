import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('growth', Path(__file__).with_name('render.py'))
growth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(growth)


class GrowthTests(unittest.TestCase):
    def snapshot(self, times):
        return {'repository': 'test/project', 'created_at': '2026-11-01T00:00:00Z',
                'as_of': '2026-11-11T12:00:00Z', 'current_stars': len(times), 'starred_at': times}

    def test_zero_is_flat(self):
        self.assertEqual([value for _, value in growth.points(self.snapshot([]))], [0, 0])

    def test_exact_steps_and_same_time_events(self):
        t = '2026-11-06T09:10:39Z'
        self.assertEqual([value for _, value in growth.points(self.snapshot([t, t]))], [0, 0, 1, 1, 2, 2])

    def test_rejects_false_totals(self):
        data = self.snapshot([])
        data['current_stars'] = 2
        with self.assertRaises(ValueError):
            growth.points(data)

    def test_smoothing_is_monotone_and_hits_real_events(self):
        times = ['2026-11-02T00:00:00Z', '2026-11-02T00:00:00Z', '2026-11-08T00:00:00Z']
        data = self.snapshot(times)
        curve = growth.smooth_points(data)
        values = [value for _, value in curve]
        self.assertEqual(values, sorted(values))
        self.assertEqual((min(values), max(values)), (0, 3))
        self.assertIn((growth.timestamp(times[0]), 2), curve)
        self.assertIn((growth.timestamp(times[2]), 3), curve)
        self.assertTrue(all(value == 0 for _, value in growth.smooth_points(self.snapshot([]))))

    def test_rejects_out_of_range_event(self):
        with self.assertRaises(ValueError):
            growth.points(self.snapshot(['2025-01-01T00:00:00Z']))

    def test_render_empty_and_one(self):
        with tempfile.TemporaryDirectory() as directory:
            for times in [[], ['2026-11-06T09:10:39Z']]:
                output = Path(directory)/'chart.png'
                growth.render(self.snapshot(times), output)
                with growth.Image.open(output) as image:
                    self.assertEqual(image.size, (1800, 660))
                self.assertTrue(output.with_suffix('.json').exists())

    def test_rest_failure_falls_back_without_user_identity(self):
        denied = growth.urllib.error.HTTPError('test', 403, 'denied', {}, None)
        result = {'data': {'repository': {'stargazers': {'edges': [{'starredAt': '2026-11-06T09:10:39Z'}],
                   'pageInfo': {'hasNextPage': False, 'endCursor': None}}}}}
        with patch.object(growth, 'request', side_effect=[denied, result]):
            times, source = growth.fetch_times('test/project', 'fake-test-token')
        self.assertEqual(len(times), 1)
        self.assertEqual(source, 'GraphQL stargazers')

    def test_count_mismatch_is_not_published(self):
        with patch.object(growth, 'request', return_value={'stargazers_count': 2}), patch.object(
                growth, 'fetch_times', return_value=([], 'test')):
            with self.assertRaises(ValueError):
                growth.fetch('test/project', 'fake-test-token')


if __name__ == '__main__':
    unittest.main()
