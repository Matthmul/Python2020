class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):
    if top is None:
        raise ValueError("puste drzewo")
    while top.right:
        top = top.right
    return top


def bst_min(top):
    if top is None:
        raise ValueError("puste drzewo")
    while top.left:
        top = top.left
    return top


import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.root_1 = None
        self.root_2 = Node(1)
        self.root_3 = Node(5)
        self.root_3.left = Node(2)
        self.root_3.right = Node(7)
        self.root_3.left.left = Node(1)
        self.root_3.left.right = Node(3)
        self.root_3.right.left = Node(6)
        self.root_3.right.right = Node(8)

    def test_bst_max(self):
        try:
            self.assertEqual("{}".format(bst_max(self.root_1)), "1")
        except:
            pass
        self.assertEqual("{}".format(bst_max(self.root_2)), "1")
        self.assertEqual("{}".format(bst_max(self.root_3)), "8")

    def test_bst_min(self):
        try:
            self.assertEqual("{}".format(bst_min(self.root_1)), "1")
        except:
            pass
        self.assertEqual("{}".format(bst_min(self.root_2)), "1")
        self.assertEqual("{}".format(bst_min(self.root_3)), "1")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
