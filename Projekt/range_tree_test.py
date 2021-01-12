from Projekt.range_tree import RangeTree

import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.rangetree = RangeTree()

        self.rangetree_1 = RangeTree(10)

        self.rangetree_2 = RangeTree(42)
        self.rangetree_2.insert(21)
        self.rangetree_2.insert(57)
        self.rangetree_2.insert(15)
        self.rangetree_2.insert(33)
        self.rangetree_2.insert(52)
        self.rangetree_2.insert(65)
        self.rangetree_2.insert(6)
        self.rangetree_2.insert(17)
        self.rangetree_2.insert(24)
        self.rangetree_2.insert(42)
        self.rangetree_2.insert(51)
        self.rangetree_2.insert(57)
        self.rangetree_2.insert(65)
        self.rangetree_2.insert(73)
        self.rangetree_2.insert(6)
        self.rangetree_2.insert(15)
        self.rangetree_2.insert(17)
        self.rangetree_2.insert(21)
        self.rangetree_2.insert(24)
        self.rangetree_2.insert(33)
        self.rangetree_2.insert(51)
        self.rangetree_2.insert(52)
        self.rangetree_2.insert(73)
        self.rangetree_2.insert(78)

        self.rangetree_3 = RangeTree()
        for i in range(20, 40):
            self.rangetree_3.insert(i)
        for i in range(0, 20):
            self.rangetree_3.insert(i)

    def test_insert_and_print(self):
        self.rangetree_1.insert(5)
        self.rangetree_1.insert(11)
        self.assertEqual(self.rangetree_1.inorder_traversal(), [5, 10, 11])
        self.assertEqual(self.rangetree_1.preorder_traversal(), [10, 5, 11])
        self.assertEqual(self.rangetree_1.postorder_traversal(), [5, 11, 10])

    def test_find(self):
        with self.assertRaises(Exception) as cm:
            self.assertEqual(self.rangetree.find(20), False)
        the_exception = cm.exception
        self.assertEqual(str(the_exception.args[0]), "Empty tree")

        self.assertEqual(self.rangetree_1.find(10), True)
        self.assertEqual(self.rangetree_1.find(20), False)

        self.assertEqual(self.rangetree_2.find(10), False)
        self.assertEqual(self.rangetree_2.find(21), True)

    def test_range_searching(self):
        with self.assertRaises(Exception) as cm:
            self.assertEqual(self.rangetree.range_searching(1, 23), [])
        the_exception = cm.exception
        self.assertEqual(str(the_exception.args[0]), "Empty tree")

        self.assertEqual(self.rangetree_1.range_searching(15, 500), [])
        self.assertEqual(self.rangetree_1.range_searching(0, 500), [10])
        self.assertEqual(self.rangetree_1.range_searching(-10, 500), [10])

        with self.assertRaises(Exception) as cm:
            self.assertEqual(self.rangetree_1.range_searching(10, 3), [])
        the_exception = cm.exception
        self.assertEqual(str(the_exception.args[0]), "Wrong scope")

        self.assertEqual(self.rangetree_2.range_searching(20, 30), [21, 21, 24, 24])
        self.assertEqual(self.rangetree_2.range_searching(20, 40), [21, 21, 33, 24, 33, 24])
        self.assertEqual(self.rangetree_2.range_searching(10, 50), [42, 21, 15, 15, 17, 17, 21, 33, 24, 24, 33, 42])
        self.assertEqual(self.rangetree_2.range_searching(60, 80), [65, 65, 73, 78, 73])
        self.assertEqual(self.rangetree_2.range_searching(0, 5), [])
        self.assertEqual(self.rangetree_2.range_searching(22, 23), [])
        self.assertEqual(self.rangetree_2.range_searching(100, 105), [])
        self.assertEqual(self.rangetree_2.range_searching(57, 57), [57])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
