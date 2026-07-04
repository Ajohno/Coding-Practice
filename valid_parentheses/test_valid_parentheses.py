import unittest
from valid_parentheses import isValid


class TestValidParentheses(unittest.TestCase):
    def test_single_pair(self):
        self.assertTrue(isValid("()"))

    def test_multiple_valid_pairs(self):
        self.assertTrue(isValid("()[]{}"))

    def test_wrong_closing_type(self):
        self.assertFalse(isValid("(]"))

    def test_valid_nested_brackets(self):
        self.assertTrue(isValid("([])"))

    def test_invalid_crossed_brackets(self):
        self.assertFalse(isValid("([)]"))

    def test_unclosed_open_bracket(self):
        self.assertFalse(isValid("("))

    def test_closing_without_opening(self):
        self.assertFalse(isValid("]"))

    def test_deeply_nested_valid(self):
        self.assertTrue(isValid("{[()()]}"))


if __name__ == "__main__":
    unittest.main()
