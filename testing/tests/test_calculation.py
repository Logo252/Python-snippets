# -*- coding: utf-8 -*-

import unittest

from testing import calculation as calc


class TestMultiply(unittest.TestCase):
    """Test for the 'multiply' function."""

    def test_with_correct_values(self):
        """Should not raise any errors."""
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


@unittest.skip  # no reason needed
class TestAdd(unittest.TestCase):
    """Test for the 'add' function."""

    def test_with_correct_values(self):
        """Should not raise any errors."""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


# @unittest.skip("Reason for skipping a class.")
class TestSubtract(unittest.TestCase):
    """Test for the 'subtract' function."""

    def test_with_correct_values(self):
        """Should not raise any errors."""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


class TestDivide(unittest.TestCase):
    """Test for the 'divide' function."""

    # @unittest.skip("Reason for skipping a method.")
    def test_with_correct_values(self):
        """Should not raise any errors."""
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

    def test_with_zero(self):
        """Should raise ZeroDivisionError error."""
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)

# if __name__ == '__main__':
#     unittest.main()

# python -m unittest -v test_calc
