import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        # infinity cases
        if denominator == 0:
            if numerator == 0:
                raise ValueError("Indeterminate form")
            elif numerator > 0:
                numerator = 1
            else:
                numerator = -1
        # normal cases, move minus to numerator
        elif denominator < 0:
            if numerator > 0:
                numerator = - numerator
            else:
                numerator = abs(numerator)
            denominator = abs(denominator)

        gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator / gcd)
        self.denominator = int(denominator / gcd)

    def __str__(self):
        """Return fraction as a string."""
        if self.denominator == 1 or self.numerator == 0:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator = 1
        new_denominator = 1
        # infinity plus each other
        if self.denominator == 0 and frac.denominator == 0:
            if self.numerator > 0:
                if frac.numerator > 0:
                    new_numerator = 1
                elif frac.numerator < 0:
                    raise ValueError("Indeterminate form")
            elif self.numerator < 0:
                if frac.numerator > 0:
                    raise ValueError("Indeterminate form")
                elif frac.numerator < 0:
                    new_numerator = -1
            new_denominator = 0
        # normal cases and any number + (+/-) infinity case
        else:
            new_numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
            new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction."""
        # indeterminate form
        if self.denominator == 0:
            if frac.numerator == 0:
                raise ValueError("Indeterminate form")
        # normal cases
        new_numerator = self.numerator * frac.numerator
        new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator

# print(Fraction(0) * Fraction(1, 0))
# print(Fraction(1, 0) * Fraction(0))
