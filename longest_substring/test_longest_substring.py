import unittest
from longest_substring import lengthOfLongestSubstring


class TestLongestSubstring(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_two(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_three(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(lengthOfLongestSubstring(""), 0)

    def test_duplicate_after_window_moves(self):
        self.assertEqual(lengthOfLongestSubstring("dvdf"), 3)

    def test_space_character(self):
        self.assertEqual(lengthOfLongestSubstring("a b c a"), 5)


if __name__ == "__main__":
    unittest.main()
