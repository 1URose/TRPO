"""Unit tests for calculator operations."""

import unittest

from LR2.calculator import add, divide, multiply, power, subtract


class CalculatorTests(unittest.TestCase):
    """Check every supported calculator operation."""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(divide(9, 2), 4.5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_of_zero(self):
        self.assertEqual(power(7, 0), 1)

    def test_power_with_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)

    def test_zero_to_negative_power_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)


if __name__ == "__main__":
    unittest.main()
