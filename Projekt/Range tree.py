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

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
