
# https://github.com/kikzu/lab11-OG-OG
# Partner 1: Omer Kayra Gungor
# Partner 2: Omer Kayra Gungor

import unittest
from calculator import (
    add, sub, mul, div,
    logarithm, exp, hypotenuse, sqrt
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-10, 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)

    def test_multiply(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-3, 4), -12)

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
        self.assertEqual(sqrt(144), 12)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(3, 8), -5)


if __name__ == "__main__":
    unittest.main()
