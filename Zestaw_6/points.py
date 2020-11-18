import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)



import unittest


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p00 = Point(0, 0)
        self.p11 = Point(1, 1)
        self.p01 = Point(0, 1)
        self.p10 = Point(1, 0)
        self.p12 = Point(1, 2)
        self.p_1_1 = Point(-1, -1)
        self.p_2_2 = Point(-2, -2)
        self.p0_1 = Point(0, -1)
        self.p_1_0 = Point(-1, 0)
        self.p_11 = Point(-1, 1)

    def test_str(self):
        self.assertEqual("(0, 0)", str(self.p00))
        self.assertEqual("(-1, -1)", str(self.p_1_1))
        self.assertEqual("(1, 1)", str(self.p11))

    def test_repr(self):
        self.assertEqual("Point(0, 0)", repr(self.p00))
        self.assertEqual("Point(-1, -1)", repr(self.p_1_1))
        self.assertEqual("Point(1, 1)", repr(self.p11))

    def test_eq(self):
        self.assertFalse(self.p_1_1 == self.p00)
        self.assertTrue(self.p00 == self.p00)
        self.assertTrue(self.p01 == self.p01)
        self.assertFalse(self.p11 == self.p12)

    def test_ne(self):
        self.assertTrue(self.p_1_1 != self.p00)
        self.assertFalse(self.p00 != self.p00)
        self.assertFalse(self.p01 != self.p01)
        self.assertTrue(self.p11 != self.p12)

    def test_add(self):
        self.assertEqual(self.p00, self.p00 + self.p00)
        self.assertEqual(self.p12, self.p11 + self.p01)
        self.assertEqual(self.p00, self.p_1_1 + self.p11)
        self.assertEqual(self.p_1_1, self.p_1_0 + self.p0_1)

    def test_sub(self):
        self.assertEqual(self.p00, self.p00 - self.p00)
        self.assertEqual(self.p10, self.p11 - self.p01)
        self.assertEqual(self.p_2_2, self.p_1_1 - self.p11)
        self.assertEqual(self.p_11, self.p_1_0 - self.p0_1)

    def test_mul(self):
        self.assertEqual(0, self.p00 * self.p00)
        self.assertEqual(1, self.p11 * self.p01)
        self.assertEqual(-2, self.p_1_1 * self.p11)
        self.assertEqual(0, self.p_1_0 * self.p0_1)

    def test_cross(self):
        self.assertEqual(0, self.p00.cross(self.p00))
        self.assertEqual(1, self.p11.cross(self.p01))
        self.assertEqual(0, self.p_1_1.cross(self.p11))
        self.assertEqual(1, self.p_1_0.cross(self.p0_1))

    def test_len(self):
        self.assertEqual(0, self.p00.length())
        self.assertEqual(1.41, round(self.p11.length(), 2))
        self.assertEqual(1.41, round(self.p_1_1.length(), 2))
        self.assertEqual(1.0, self.p_1_0.length())

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
