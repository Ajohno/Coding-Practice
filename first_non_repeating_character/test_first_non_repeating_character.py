import unittest

from first_non_repeating_character import first_non_repeating_character


class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(first_non_repeating_character("leetcode"), 0)

    def test_example_two(self):
        self.assertEqual(first_non_repeating_character("loveleetcode"), 2)

    def test_no_unique_character(self):
        self.assertEqual(first_non_repeating_character("aabb"), -1)

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character("z"), 0)

    def test_empty_string(self):
        self.assertEqual(first_non_repeating_character(""), -1)


if __name__ == "__main__":
    unittest.main()
