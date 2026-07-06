import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from longest_unique_prefix import longest_unique_prefix


class TestLongestUniquePrefix(unittest.TestCase):
    def test_all_unique(self):
        self.assertEqual(longest_unique_prefix("abcdef"), 6)

    def test_repeat_after_unique_prefix(self):
        self.assertEqual(longest_unique_prefix("abcaef"), 3)

    def test_all_same_character(self):
        self.assertEqual(longest_unique_prefix("aaaa"), 1)

    def test_empty_string(self):
        self.assertEqual(longest_unique_prefix(""), 0)

    def test_single_character(self):
        self.assertEqual(longest_unique_prefix("z"), 1)

    def test_repeat_second_character(self):
        self.assertEqual(longest_unique_prefix("aabc"), 1)

    def test_late_repeat(self):
        self.assertEqual(longest_unique_prefix("xyzxy"), 3)


if __name__ == "__main__":
    unittest.main()
