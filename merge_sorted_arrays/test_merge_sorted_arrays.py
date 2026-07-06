import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from merge_sorted_arrays import merge_sorted_arrays


class TestMergeSortedArrays(unittest.TestCase):
    def test_interleaved_values(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_first_array_empty(self):
        self.assertEqual(merge_sorted_arrays([], [1, 2, 3]), [1, 2, 3])

    def test_second_array_empty(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 3], []), [1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 2], [2, 2, 3]), [1, 2, 2, 2, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_arrays([-5, -2, 0], [-4, -1, 3]), [-5, -4, -2, -1, 0, 3])

    def test_both_empty(self):
        self.assertEqual(merge_sorted_arrays([], []), [])


if __name__ == "__main__":
    unittest.main()
