import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        """Test of __str__"""
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        # infinity cases
        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-1/0", f.__str__())
        f = Fraction(3, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-3, 0)
        self.assertEqual("-1/0", f.__str__())

    def test_add(self):
        """Test of __add__ (+)"""
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(-1), Fraction(-1, 3) + Fraction(-2, 3))
        self.assertEqual(Fraction(0), Fraction(4, 5) + Fraction(-4, 5))
        self.assertEqual(Fraction(-1, 90), Fraction(23, -45) + Fraction(1, 2))
        self.assertEqual(Fraction(0, 1), Fraction(0) + Fraction(0))
        self.assertEqual(Fraction(7), Fraction(7) + Fraction(0))
        # infinity cases
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(5, 2))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) + Fraction(5, 2))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(1, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) + Fraction(-1, 0))
        # indeterminate forms
        with self.assertRaises(ValueError):
            Fraction(1, 0) + Fraction(-1, 0)
            Fraction(-1, 0) + Fraction(1, 0)

    def test_init(self):
        """Test of __init__"""
        f = Fraction(1, 2)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(-1, -2)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(-1, 2)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(1, -2)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(2, f.denominator)
        # numerator and denominator have common factor
        f = Fraction(5, 10)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(10, 5)
        self.assertEqual(2, f.numerator)
        self.assertEqual(1, f.denominator)
        # default denominator
        f = Fraction(0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(50)
        self.assertEqual(50, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(-50)
        self.assertEqual(-50, f.numerator)
        self.assertEqual(1, f.denominator)
        # infinity case
        f = Fraction(1, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-1, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(3, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-3, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        # indeterminate form
        with self.assertRaises(ValueError):
            Fraction(0, 0)

    def test_mul(self):
        """Test of __mul__ (*)"""
        self.assertEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))
        self.assertEqual(Fraction(-1, 4), Fraction(-1, 2) * Fraction(1, 2))
        self.assertEqual(Fraction(1, 4), Fraction(-1, 2) * Fraction(-1, 2))
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(1, 2))
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(-1, 2))
        self.assertEqual(Fraction(1, 2), Fraction(1) * Fraction(1, 2))
        self.assertEqual(Fraction(-1, 2), Fraction(1) * Fraction(-1, 2))
        # infinity cases
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(5, 7))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) * Fraction(5, 7))
        self.assertEqual(Fraction(1, 0), Fraction(-1, 0) * Fraction(-5, 7))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(1, 0))
        self.assertEqual(Fraction(1, 0), Fraction(-1, 0) * Fraction(-1, 0))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) * Fraction(1, 0))
        # indeterminate forms
        with self.assertRaises(ValueError):
            Fraction(0) * Fraction(1, 0)
            Fraction(0) * Fraction(-1, 0)

    def test_eq(self):
        """Test of __eq__ (==)"""
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        f = Fraction(3, 4)
        g = Fraction(-9, -12)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        f = Fraction(3, 4)
        g = Fraction(-3, 4)
        self.assertFalse(f == g)
        self.assertFalse(f.__eq__(g))
        f = Fraction(0)
        g = Fraction(0, 1)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        f = Fraction(-3, -4)
        g = Fraction(-3, -4)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        f = Fraction(1, 0)
        g = Fraction(-1, 0)
        self.assertFalse(f == g)
        self.assertFalse(f.__eq__(g))
        f = Fraction(3, 0)
        g = Fraction(1, 0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
