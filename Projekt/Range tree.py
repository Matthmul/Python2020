from Projekt.Node import Node


class RangeTree:
    """
    Klasa reprezentująca range tree. Pozwala na utworzenie drzewa bez korzenia.

    ...

    Attributes
    --------
    root : Node, int
        Korzen dla drzewa, jesli podana zostanie liczba zostanie utworzony przy pomocy niej Node

    Methods
    -------
    insert(data)
        Dadanie podanej liczby do drzewa

    find(data)
        Sprawdzenie czy istnieje dna liczba w drzewie

    range_searching(x1, x2)
        Przeszukanie i zwrocenie liczb z podanego zakresu

    print_tree()
        Wypisanie drzewa w klojenosci inorder

    inorder_traversal()
        Zwrocenie tablicy z elementami drzewa w kolejnosci inorder

    preorder_traversal()
        Zwrocenie tablicy z elementami drzewa w kolejnosci preorder

    postorder_traversal()
        Zwrocenie tablicy z elementami drzewa w kolejnosci postorder

    """

    def __init__(self, root=None):
        """
        Parameters
        ----------
        root : Node, int
            Node ktory bedzie korzeniem
        """

        if root is not None:
            if type(root) == int:
                root = Node(root)
            if type(root) != Node:
                raise Exception("Wrong type of variable")
        self.root = root

    def insert(self, data):
        """Dodanie nowej wartosci do drzewa

        Parameters
        ----------
        data : Node, int
            Liczba lub Node ktory bedzie dodany do drzewa
        """

        if type(data) == int:
            data = Node(data)

        if self.root is None:
            self.root = data
        else:
            self.__insert_node(self.root, data)

    def __insert_node(self, current_node, node):
        """Funkcja umieszczajaca Noda w odpowiednim miejscu

        Parameters
        ----------
        current_node : Node
            Liczba lub Node ktory bedzie dodany do drzewa
        node : Node
            Liczba lub Node ktory bedzie dodany do drzewa
        """

        if node.data <= current_node.data:
            if current_node.left is None:
                current_node.left = node
            else:
                self.__insert_node(current_node.left, node)
        else:  # data > current_node.data:
            if current_node.right is None:
                current_node.right = node
            else:
                self.__insert_node(current_node.right, node)

    def find(self, data):
        """Sprawdza czy podana liczba lub Node znjaduje sie w drzewie

        Parameters
        ----------
        data : Node, int
            The sound the animal makes (default is None)

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia

        Returns
        -------
        bool
            True jesli istnieje, False jesli nie istnieje
        """

        if type(data) == int:
            data = Node(data)

        if self.root is None:
            raise Exception("Empty tree")
        return self.__find_node(self.root, data)

    def __find_node(self, current_node, node):
        """Funkcja pomocnicza starajaca sie zlokalizowac podanego Noda

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajduje funkcja
        node : Node
            Szukany Node

        Returns
        -------
        bool
            True jesli istnieje, False jesli nie istnieje
        """

        if current_node is None:
            return False
        elif node.data == current_node.data:
            return True
        elif node.data <= current_node.data:
            return self.__find_node(current_node.left, node)
        else:
            return self.__find_node(current_node.right, node)

    def range_searching(self, x1, x2):
        """Przeszukiwanie drzewa dla liczb z zakresu [x1, x2]

        Parameters
        ----------
        x1 : int
            Poczatek zakresu
        x2 : int
            Koniec zkaresu

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia
        ValueError
            Jeśli podano bledny zakres

        Returns
        -------
        list
            Tablica liczb ktore dla podanego zakresu znajduja sie w drzewie
        """

        if self.root is None:
            raise Exception("Empty tree")
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

    def __range_searching_left(self, current_node, x1):
        """Funkcja pomocnicza ktora dodaje do listy wszytkie nody znajdujace sie na lewo od Noda rozdzielajacego

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        x1 : int
            Poczatek zkaresu

        Returns
        -------
        list
            Tablica liczb ktore na lewo on Noda rozdzielajacego znajduja sie w drzewie
        """

        res = []
        if x1 <= current_node.data:
            res.append(current_node.data)
            if current_node.left is not None:
                res = res + self.__range_searching_left(current_node.left, x1)
            if current_node.right is not None:
                res = res + self.__range_searching_left(current_node.right, x1)
        elif current_node.right is not None:
            res = self.__range_searching_left(current_node.right, x1)
        return res

    def __range_searching_right(self, current_node, x2):
        """Funkcja pomocnicza ktora dodaje do listy wszytkie nody znajdujace sie na prawo od Noda rozdzielajacego

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        x2 : int
            Koniec zkaresu

        Returns
        -------
        list
            Tablica liczb ktore na prawo on Noda rozdzielajacego znajduja sie w drzewie
        """

        res = []
        if x2 >= current_node.data:
            res.append(current_node.data)
            if current_node.right is not None:
                res = res + self.__range_searching_right(current_node.right, x2)
            if current_node.left is not None:
                res = res + self.__range_searching_right(current_node.left, x2)
        elif current_node.left is not None:
            res = self.__range_searching_right(current_node.left, x2)
        return res

    def __find_x_split(self, current_node, x1, x2):
        """Funkcja pomocnicza ktora znajduje od Noda rozdzielajacego

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        x1 : int
            Poczatek zkaresu
        x2 : int
            Koniec zkaresu

        Returns
        -------
        Node
            Zwraca Noda rozdzielajacego jesli takiego znajdzie
        """

        if not current_node.is_leaf() and (x2 <= current_node.data or x1 > current_node.data):
            if x2 <= current_node.data and current_node.left is not None:
                return self.__find_x_split(current_node.left, x1, x2)
            elif current_node.right is not None:
                return self.__find_x_split(current_node.right, x1, x2)
        return current_node

    def print_tree(self):
        """Funkcja wyswietlajaca drzewo w kolejnosci inorder

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia
        """

        if self.root is None:
            raise Exception("Empty tree")
        self.__print_tree_node(self.root)

    def __print_tree_node(self, current_node):
        """Funkcja pomocnicza wypiujaca zawartosc Noda

        """

        if current_node.left:
            self.__print_tree_node(current_node.left)
        print(current_node.data)
        if current_node.right:
            self.__print_tree_node(current_node.right)

    def inorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci inorder

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci inorder
        """

        if self.root is None:
            raise Exception("Empty tree")
        return self.__inorder_traversal(self.root)

    def __inorder_traversal(self, current_node):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci inorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci inorder dla aktualnego Noda
        """

        res = []
        if current_node:
            res = self.__inorder_traversal(current_node.left)
            res.append(current_node.data)
            res = res + self.__inorder_traversal(current_node.right)
        return res

    def preorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci preorder

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci preorder
        """

        if self.root is None:
            raise Exception("Empty tree")
        return self.__preorder_traversal(self.root)

    def __preorder_traversal(self, current_node):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci preorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci preorder dla aktualnego Noda
        """

        res = []
        if current_node:
            res.append(current_node.data)
            res = res + self.__preorder_traversal(current_node.left)
            res = res + self.__preorder_traversal(current_node.right)
        return res

    def postorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci postorder

        Raises
        ------
        Exception
            Jeśli drzewo nie posiada korzenia

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci postorder
        """

        if self.root is None:
            raise Exception("Empty tree")
        return self.__postorder_traversal(self.root)

    def __postorder_traversal(self, current_node):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci postorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci postorder dla aktualnego Noda
        """

        res = []
        if current_node:
            res = self.__postorder_traversal(current_node.left)
            res = res + self.__postorder_traversal(current_node.right)
            res.append(current_node.data)
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
