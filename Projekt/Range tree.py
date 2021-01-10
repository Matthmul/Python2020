from Projekt.Node import Node


class RangeTree:
    """Klasa reprezentująca range tree."""

    def __init__(self, root=None):
        if root is not None:
            if type(root) == int:
                root = Node(root)
            if type(root) != Node:
                raise Exception("Wrong type of variable")
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert_node(self.root, data)

    def __insert_node(self, current_node, data):
        if data <= current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.__insert_node(current_node.left, data)
        else:  # data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.__insert_node(current_node.right, data)

    def __add__(self, other):
        pass

    def find(self, data):
        if self.root is None:
            raise Exception("Empty tree")
        return self.__find_node(self.root, data)

    def __find_node(self, current_node, data):
        if current_node is None:
            return False
        elif data == current_node.data:
            return True
        elif data <= current_node.data:
            return self.__find_node(current_node.left, data)
        else:
            return self.__find_node(current_node.right, data)

    def range_searching(self, x1, x2):
        if x1 > x2:
            raise ValueError("Zly zakres")
        res = []
        root = self.__find_x_split(self.root, x1, x2)
        if root.is_leaf():
            if x1 <= root.data <= x2:
                res.append(root.data)
            return res
        else:
            res.append(root.data)
            res = res + self.__range_searching_left(root.left, x1)
            res = res + self.__range_searching_right(root.right, x2)
            return res

    def __range_searching_left(self, root, x1):
        res = []
        if x1 <= root.data:
            res.append(root.data)
            if root.left is not None:
                res = res + self.__range_searching_left(root.left, x1)
            if root.right is not None:
                res = res + self.__range_searching_left(root.right, x1)
        elif root.right is not None:
            res = self.__range_searching_left(root.right, x1)
        return res

    def __range_searching_right(self, root, x2):
        res = []
        if x2 >= root.data:
            res.append(root.data)
            if root.right is not None:
                res = res + self.__range_searching_right(root.right, x2)
            if root.left is not None:
                res = res + self.__range_searching_right(root.left, x2)
        elif root.left is not None:
            res = self.__range_searching_right(root.left, x2)
        return res

    def __find_x_split(self, root, x1, x2):
        if not root.is_leaf() and (x2 <= root.data or x1 > root.data):
            if x2 <= root.data and root.left is not None:
                return self.__find_x_split(root.left, x1, x2)
            elif root.right is not None:
                return self.__find_x_split(root.right, x1, x2)
        return root

    def print_tree(self):
        if self.root is None:
            raise Exception("Empty tree")
        self.__print_tree_node(self.root)

    def __print_tree_node(self, root):
        if root.left:
            self.__print_tree_node(root.left)
        print(root.data)
        if root.right:
            self.__print_tree_node(root.right)

    def inorder_traversal(self):
        if self.root is None:
            raise Exception("Empty tree")
        return self.__inorder_traversal(self.root)

    def __inorder_traversal(self, root):
        res = []
        if root:
            res = self.__inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.__inorder_traversal(root.right)
        return res

    def preorder_traversal(self):
        if self.root is None:
            raise Exception("Empty tree")
        return self.__preorder_traversal(self.root)

    def __preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.__preorder_traversal(root.left)
            res = res + self.__preorder_traversal(root.right)
        return res

    def postorder_traversal(self):
        if self.root is None:
            raise Exception("Empty tree")
        return self.__postorder_traversal(self.root)

    def __postorder_traversal(self, root):
        res = []
        if root:
            res = self.__postorder_traversal(root.left)
            res = res + self.__postorder_traversal(root.right)
            res.append(root.data)
        return res


import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.rangetree = RangeTree()
        self.rangetree_10 = RangeTree(10)
        self.rangetree_20 = RangeTree(42)
        self.rangetree_40 = RangeTree()
        self.rangetree_20.insert(21)
        self.rangetree_20.insert(57)
        self.rangetree_20.insert(15)
        self.rangetree_20.insert(33)
        self.rangetree_20.insert(52)
        self.rangetree_20.insert(65)
        self.rangetree_20.insert(6)
        self.rangetree_20.insert(17)
        self.rangetree_20.insert(24)
        self.rangetree_20.insert(42)
        self.rangetree_20.insert(51)
        self.rangetree_20.insert(57)
        self.rangetree_20.insert(65)
        self.rangetree_20.insert(73)
        self.rangetree_20.insert(6)
        self.rangetree_20.insert(15)
        self.rangetree_20.insert(17)
        self.rangetree_20.insert(21)
        self.rangetree_20.insert(24)
        self.rangetree_20.insert(33)
        self.rangetree_20.insert(51)
        self.rangetree_20.insert(52)
        self.rangetree_20.insert(73)
        self.rangetree_20.insert(78)
        for i in range(20, 40):
            self.rangetree_40.insert(i)
        for i in range(0, 20):
            self.rangetree_40.insert(i)

    def test_insert(self):
        self.rangetree_10.insert(5)
        self.rangetree_10.insert(11)
        self.assertEqual(self.rangetree_10.inorder_traversal(), [5, 10, 11])
        self.assertEqual(self.rangetree_10.preorder_traversal(), [10, 5, 11])
        self.assertEqual(self.rangetree_10.postorder_traversal(), [5, 11, 10])

    def test_find(self):
        self.assertEqual(self.rangetree_10.find(10), True)
        self.assertEqual(self.rangetree_10.find(20), False)
        with self.assertRaises(Exception) as cm:
            self.assertEqual(self.rangetree.find(20), False)
        the_exception = cm.exception
        self.assertEqual(str(the_exception.args[0]), "Empty tree")

    def test_range_searching(self):
        self.assertEqual(self.rangetree_20.range_searching(20, 30), [21, 21, 24, 24])
        self.assertEqual(self.rangetree_20.range_searching(20, 40), [21, 21, 33, 24, 33, 24])
        self.assertEqual(self.rangetree_20.range_searching(10, 50), [42, 21, 15, 15, 17, 17, 21, 33, 24, 24, 33, 42])
        self.assertEqual(self.rangetree_20.range_searching(60, 80), [65, 65, 73, 78, 73])
        self.assertEqual(self.rangetree_20.range_searching(0, 5), [])
        self.assertEqual(self.rangetree_20.range_searching(100, 105), [])
        self.assertEqual(self.rangetree_20.range_searching(57, 57), [57])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
