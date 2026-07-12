import unittest

from product_of_array_except_self import product_except_self


class TestProductExceptSelf(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_contains_zero(self):
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_two_elements(self):
        self.assertEqual(product_except_self([2, 3]), [3, 2])

    def test_two_zeros(self):
        self.assertEqual(product_except_self([0, 4, 0]), [0, 0, 0])

    def test_negative_values(self):
        self.assertEqual(product_except_self([-2, -3, -4]), [12, 8, 6])

    def test_ones(self):
        self.assertEqual(product_except_self([1, 1, 1]), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()
