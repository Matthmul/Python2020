import math


def add_frac(frac1, frac2):
    nominator = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def sub_frac(frac1, frac2):
    nominator = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def mul_frac(frac1, frac2):
    nominator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def div_frac(frac1, frac2):
    nominator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def is_positive(frac):
    return frac[0] > 0


def is_zero(frac):
    return not frac[0]


def cmp_frac(frac1, frac2):
    gcd = math.gcd(frac1[0], frac1[1])
    frac1 = [frac1[0] / gcd, frac1[1] / gcd]
    gcd = math.gcd(frac2[0], frac2[1])
    frac2 = [frac2[0] / gcd, frac2[1] / gcd]
    if frac1[0] == frac2[0] and frac1[1] == frac2[1]:
        return 0
    elif (frac1[0] / frac1[1]) > (frac2[0] / frac2[1]):
        return 1
    else:
        return -1


def frac2float(frac):
    return float(frac[0] / frac[1])


import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 1], [4, 1]), [6, 1])
        self.assertEqual(add_frac([-2, 1], [2, 1]), self.zero)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([2, 1], [4, 1]), [-2, 1])
        self.assertEqual(sub_frac(self.zero, [2, 1]), [-2, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 1], [4, 1]), [8, 1])
        self.assertEqual(mul_frac(self.zero, [2, 1]), [0, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 1], [4, 1]), [1, 2])
        self.assertEqual(div_frac(self.zero, [2, 1]), [0, 1])

    def test_is_positive(self):
        self.assertEqual(True, is_positive([1, 5]))
        self.assertEqual(False, is_positive([-1, 5]))
        self.assertEqual(False, is_positive(self.zero))
        self.assertEqual(False, is_positive([0, 0]))

    def test_is_zero(self):
        self.assertEqual(True, is_zero(self.zero))
        self.assertEqual(False, is_zero([1, 5]))
        self.assertEqual(False, is_zero([-1, 5]))
        self.assertEqual(True, is_zero([0, 0]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 5], [1, 5]), -1)
        self.assertEqual(cmp_frac([1, 5], [1, 5]), 0)
        self.assertEqual(cmp_frac([1, 5], [-1, 5]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 8]), 0.125)
        self.assertEqual(frac2float([1, 4]), 0.25)
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 1]), 1)
        self.assertEqual(frac2float([0, 1]), 0)
        self.assertEqual(frac2float([6, 2]), 3)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
