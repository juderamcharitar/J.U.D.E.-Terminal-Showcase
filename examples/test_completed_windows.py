import unittest
from completed_windows import completed_windows


class CompletedWindowTests(unittest.TestCase):
    def test_every_eligible_outcome_finishes_by_cutoff(self):
        for window in completed_windows(31, 10, 4, 3):
            self.assertTrue(window.eligible_entries)
            for entry in window.eligible_entries:
                self.assertGreaterEqual(entry, window.start)
                self.assertLessEqual(entry + 3, window.cutoff)
            self.assertEqual(window.eligible_entries[-1] + 3, window.cutoff)

    def test_earlier_regular_windows_do_not_use_future_history(self):
        before = completed_windows(20, 10, 4, 3)
        after = completed_windows(40, 10, 4, 3)
        self.assertEqual(before[:2], after[:2])

    def test_latest_cutoff_is_included_when_step_does_not_divide_history(self):
        windows = completed_windows(21, 10, 4, 3)
        self.assertEqual(windows[-1].cutoff, 20)
        self.assertEqual(windows[-1].start, 11)

    def test_invalid_counts_are_rejected(self):
        for arguments in [(0, 10, 4, 3), (20, 0, 4, 3), (20, 10, 0, 3),
                          (20, 10, 4, 0), (20, 30, 4, 3), (20, 10, 4, 10),
                          (True, 10, 4, 3), (20, 10.5, 4, 3)]:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    completed_windows(*arguments)


if __name__ == "__main__":
    unittest.main()
