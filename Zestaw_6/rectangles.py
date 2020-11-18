from Zestaw_6.points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")"

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):  # pole powierzchni
        return abs(self.pt1.y - self.pt2.y) * abs(self.pt2.x - self.pt1.x)

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y,
                         self.pt2.x + x, self.pt2.y + y)



import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self): pass

    def setUp(self):
        self.r1 = Rectangle(1, 0, 0, -1)
        self.r2 = Rectangle(2, 0, 0, -2)
        self.r3 = Rectangle(2, 2, -2, -2)

    def test_str(self):
        self.assertEqual("[(1, 0), (0, -1)]", str(self.r1))

    def test_repr(self):
        self.assertEqual("Rectangle(1, 0, 0, -1)", repr(self.r1))

    def test_eq(self):
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r1 == self.r1)
        self.assertTrue(self.r3 == self.r3)

    def test_ne(self):
        self.assertFalse(self.r1 != self.r1)
        self.assertTrue(self.r1 != self.r2)
        self.assertTrue(self.r3 != self.r2)

    def test_center(self):
        self.assertEqual(Point(0.5, -0.5), self.r1.center())
        self.assertEqual(Point(1, -1), self.r2.center())
        self.assertEqual(Point(0.0, 0.0), self.r3.center())

    def test_area(self):
        self.assertEqual(1, self.r1.area())
        self.assertEqual(4, self.r2.area())
        self.assertEqual(16, self.r3.area())

    def test_move(self):
        self.assertEqual(Rectangle(2, -1, 1, -2), self.r1.move(1, -1))
        self.assertEqual(Rectangle(4, 0, 0, -4), self.r3.move(2, -2))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
