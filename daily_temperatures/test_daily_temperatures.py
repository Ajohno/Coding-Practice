import unittest

from daily_temperatures import daily_temperatures


class TestDailyTemperatures(unittest.TestCase):
    def test_mixed_temperatures(self):
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )

    def test_strictly_increasing(self):
        self.assertEqual(
            daily_temperatures([30, 40, 50, 60]),
            [1, 1, 1, 0],
        )

    def test_strictly_decreasing(self):
        self.assertEqual(
            daily_temperatures([60, 50, 40, 30]),
            [0, 0, 0, 0],
        )

    def test_equal_temperatures(self):
        self.assertEqual(
            daily_temperatures([70, 70, 70]),
            [0, 0, 0],
        )

    def test_single_day(self):
        self.assertEqual(daily_temperatures([75]), [0])

    def test_warmer_day_after_gap(self):
        self.assertEqual(
            daily_temperatures([70, 69, 68, 71]),
            [3, 2, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
