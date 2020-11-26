import math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y != 0:
            if isinstance(x, float) or isinstance(y, float):
                if isinstance(x, float) and isinstance(y, float):
                    self.x = x.as_integer_ratio()[0] * y.as_integer_ratio()[1]
                    self.y = y.as_integer_ratio()[0] * x.as_integer_ratio()[1]
                elif isinstance(x, float):
                    self.x = x.as_integer_ratio()[0] * y
                    self.y = y * x.as_integer_ratio()[1]
                elif isinstance(y, float):
                    self.x = x * y.as_integer_ratio()[1]
                    self.y = y.as_integer_ratio()[0] * x
            else:
                self.x = x
                self.y = y

            mgcd = math.gcd(self.x, self.y)
            if mgcd > 1:
                self.x /= mgcd
                self.y /= mgcd
            if y < 0:
                self.x = -self.x
                self.y = -self.y
        else:
            raise ValueError

    def __str__(self):
        if self.y == 1:
            return '{}'.format(self.x)
        return '{}/{}'.format(self.x, self.y)

    def __repr__(self):
        return 'Frac({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except:
            raise ValueError

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):  # frac1 + frac2, frac+int
        if isinstance(other, Frac):
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        else:
            return Frac(self.x + (other * self.y), self.y)

    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, Frac):
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        else:
            return Frac(self.x - (other * self.y), self.y)

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        else:
            return Frac(self.x * other, self.y * other)

    __rmul__ = __mul__  # int*frac

    # def __div__(self, other): pass  # frac1/frac2, frac/int, Python 2
    #
    # def __rdiv__(self, other): pass # int/frac, Python 2

    def __truediv__(self, other):  # frac1/frac2, frac/int, Python 3
        if isinstance(other, Frac):
            other.x, other.y = other.y, other.x
            return self * other
        else:
            return self * Frac(1, other)

    def __rtruediv__(self, other):  # int/frac, Python 3
        if isinstance(other, Frac):
            self.x, self.y = self.y, self.x
            return self * other
        else:
            return self * Frac(other)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y  # float(frac)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])


import unittest


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.zero = Frac(0, 1)
        self.f1 = Frac(-1, 2)
        self.f2 = Frac(0, 1)
        self.f3 = Frac(3, 1)
        self.f4 = Frac(6, 2)
        self.f5 = Frac(0, 2)
        self.f6 = Frac(1, 3)
        self.f7 = Frac(1, 6)
        self.f8 = Frac(10, 1)
        self.f9 = Frac(100, 2)
        self.f10 = Frac(6, 2)

    def test_add(self):
        self.assertEqual(Frac(1, 1) + Frac(2, 2), Frac(2, 1))
        self.assertEqual(self.f4 + self.f7, Frac(19, 6))
        self.assertEqual(self.f5 + self.f7, Frac(1, 6))
        self.assertEqual(5 + self.f7, Frac(31, 6))
        self.assertEqual(self.f5 + 5, Frac(5, 1))
        self.assertEqual(self.f5 + 5.5, Frac(11, 2))

    def test_sub(self):
        self.assertEqual(self.f8 - self.f4, Frac(7, 1))
        self.assertEqual(self.f9 - self.f3, Frac(47, 1))
        self.assertEqual(self.f9 - 10, Frac(40, 1))
        self.assertEqual(100 - self.f3, Frac(97, 1))
        self.assertEqual(self.f9 - 10.5, Frac(79, 2))

    def test_mul(self):
        self.assertEqual(self.f8 * self.f4, Frac(30, 1))
        self.assertEqual(self.f9 * self.f2, Frac(0, 1))
        self.assertEqual(self.f9 * 10, Frac(50, 1))
        self.assertEqual(10 * self.f2, Frac(0, 1))
        self.assertEqual(self.f9 * 10.5, Frac(50, 1))
        self.assertEqual(10.5 * self.f2, Frac(0, 1))

    def test_div(self):
        try:
            self.f9 / self.f2
        except Exception as inst:
            self.assertEqual(inst.__class__, ValueError)
        self.assertEqual(self.f7 / self.f3, Frac(1, 18))
        self.assertEqual(self.f7 / 5, Frac(1, 30))
        self.assertEqual(5 / self.f3, Frac(5, 3))
        self.assertEqual(self.f7 / 5.5, Frac(1, 33))

    def test_lt(self):
        self.assertEqual(self.f7 > self.f1, True)
        self.assertEqual(self.f1 < self.f6, True)
        self.assertEqual(self.f4 <= self.f4, True)
        self.assertEqual(self.f6 >= self.f2, True)

    def test_pos(self):
        self.assertEqual(+self.f7, self.f7)
        self.assertEqual(+self.f1, self.f1)
        self.assertEqual(+self.f4, self.f4)
        self.assertEqual(+self.f6, self.f6)

    def test_neg(self):
        self.assertEqual(-self.f7, Frac(-1, 6))
        self.assertEqual(-self.f1, Frac(1, 2))
        self.assertEqual(-self.f4, Frac(-3, 1))
        self.assertEqual(-self.f6, Frac(-1, 3))

    def test_invert(self):
        self.assertEqual(self.f7.__invert__(), Frac(6, 1))
        self.assertEqual(self.f1.__invert__(), Frac(-2, 1))
        self.assertEqual(self.f4.__invert__(), Frac(1, 3))
        self.assertEqual(self.f6.__invert__(), Frac(3, 1))

    def test_float(self):
        try:
            self.assertEqual(self.f7.__float__(), Frac(6, 1))
        except Exception as inst:
            self.assertEqual(inst.__class__, ValueError)
        self.assertEqual(self.f1.__float__(), -0.5)
        self.assertEqual(self.f4.__float__(), 3)
        self.assertEqual(self.f2.__float__(), 0)

    def test_hash(self):
        try:
            self.assertEqual(self.f7.__hash__(), Frac(6, 1))
        except Exception as inst:
            self.assertEqual(inst.__class__, ValueError)
        self.assertEqual(self.f1.__hash__(), hash(-0.5))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
