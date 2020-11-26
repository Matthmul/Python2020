from Zestaw_6.points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError
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

    def intersection(self, other):  # część wspólna prostokątów
        x1 = max(min(self.pt1.x, self.pt2.x), min(other.pt1.x, other.pt2.x))
        y1 = max(min(self.pt1.y, self.pt2.y), min(other.pt1.y, other.pt2.y))
        x2 = min(max(self.pt1.x, self.pt2.x), max(other.pt1.x, other.pt2.x))
        y2 = min(max(self.pt1.y, self.pt2.y), max(other.pt1.y, other.pt2.y))
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):  # prostąkąt nakrywający oba
        x1 = min(min(self.pt1.x, self.pt2.x), min(other.pt1.x, other.pt2.x))
        y1 = min(min(self.pt1.y, self.pt2.y), min(other.pt1.y, other.pt2.y))
        x2 = max(max(self.pt1.x, self.pt2.x), max(other.pt1.x, other.pt2.x))
        y2 = max(max(self.pt1.y, self.pt2.y), max(other.pt1.y, other.pt2.y))
        return Rectangle(x1, y1, x2, y2)

    def make4(self):  # zwraca krotkę czterech mniejszych
        cntr = self.center()
        return [Rectangle(self.pt1.x, self.pt1.y, cntr.x, cntr.y), Rectangle(self.pt1.x, cntr.y, cntr.x, self.pt2.y),
                Rectangle(cntr.x, self.pt1.y, self.pt2.x, cntr.y), Rectangle(cntr.x, cntr.y, self.pt2.x, self.pt2.y)]


import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self): pass

    def setUp(self):
        self.r1 = Rectangle(0, 1, 1, 2)
        self.r2 = Rectangle(0, 2, 2, 4)
        self.r3 = Rectangle(-2, 3, 0, 6)
        self.r4 = Rectangle(-10, -10, 10, 10)

    def test_str(self):
        self.assertEqual("[(0, 1), (1, 2)]", str(self.r1))

    def test_repr(self):
        self.assertEqual("Rectangle(0, 1, 1, 2)", repr(self.r1))

    def test_eq(self):
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r1 == self.r1)
        self.assertTrue(self.r3 == self.r3)

    def test_ne(self):
        self.assertFalse(self.r1 != self.r1)
        self.assertTrue(self.r1 != self.r2)
        self.assertTrue(self.r3 != self.r2)

    def test_center(self):
        self.assertEqual(Point(0.5, 1.5), self.r1.center())
        self.assertEqual(Point(1, 3), self.r2.center())
        self.assertEqual(Point(-1.0, 4.5), self.r3.center())

    def test_area(self):
        self.assertEqual(1, self.r1.area())
        self.assertEqual(4, self.r2.area())
        self.assertEqual(6, self.r3.area())

    def test_move(self):
        self.assertEqual(Rectangle(1, 0, 2, 1), self.r1.move(1, -1))
        self.assertEqual(Rectangle(0, 1, 2, 4), self.r3.move(2, -2))

    def test_intersection(self):
        try:
            self.assertEqual(Rectangle(0, 1, 2, 4), self.r1.intersection(self.r2))
        except Exception as inst:
            self.assertEqual(inst.__class__, ValueError)
        self.assertEqual(Rectangle(0, 1, 1, 2), self.r4.intersection(self.r1))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 1, 2, 4), self.r1.cover(self.r2))
        self.assertEqual(Rectangle(-2, 1, 1, 6), self.r3.cover(self.r1))

    def test_make4(self):
        self.assertEqual([Rectangle(0, 1, 0.5, 1.5),
                          Rectangle(0, 1.5, 0.5, 2),
                          Rectangle(0.5, 1, 1, 1.5),
                          Rectangle(0.5, 1.5, 1, 2)], self.r1.make4())
        self.assertEqual([Rectangle(-2, 3, -1.0, 4.5),
                          Rectangle(-2, 4.5, -1.0, 6),
                          Rectangle(-1.0, 3, 0, 4.5),
                          Rectangle(-1.0, 4.5, 0, 6)], self.r3.make4())

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
