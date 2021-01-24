from Projekt.node import Node


class RangeTree:
    """
    Klasa reprezentująca range tree. Pozwala na utworzenie drzewa bez korzenia.

    ...

    Attributes
    --------
    root
        Korzen dla drzewa, jesli podana zostanie liczba zostanie utworzony przy pomocy niej Node

    Methods
    -------
    insert(data)
        Dadanie podanej liczby do drzewa

    delete(data)
        Usuniecie podanej liczby do drzewa

    minimum_value(current_node)
        Wyszukanie najmniejszej wartosci

    maximum_value(current_node)
        Wyszukanie najwiekszej wartosci

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

    def __init__(self, *datas):
        """
        Parameters
        ----------
        root
            Node ktory bedzie korzeniem
        """
        self.root = None
        for data in datas:
            self.insert(data)

    def insert(self, data):
        """Dodanie nowej wartosci do drzewa

        Parameters
        ----------
        data
            Liczba lub Node ktory bedzie dodany do drzewa
        """

        if type(data) != Node:
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

    def delete(self, node):
        """Usuniecie wartosci z drzewa

        Parameters
        ----------
        node
            Liczba lub Node ktory bedzie dodany do drzewa

        Returns
        -------
        bool
            True jesli usunieto, False jesli nie usunieto
        """

        if type(node) != Node:
            node = Node(node)

        parent = None
        curr = self.root

        while curr is not None and curr.data != node.data:
            parent = curr
            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return False

        if curr.left is None and curr.right is None:

            if curr != self.root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            else:
                self.root = None

        elif curr.left and curr.right:
            successor = self.minimum_value(curr.right)
            val = successor
            self.delete(successor)
            curr.data = val

        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            if curr != self.root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        return True

    def minimum_value(self, current_node=None):
        """Szuka najmniejszej wartosci w drzewie

        Parameters
        ----------
        current_node : Node
            Aktualny node

        Returns
        -------
        number
            Zawartosc najmniejszeogo noda
        """
        if self.root is None:
            return None

        if current_node is None:
            current_node = self.root

        if current_node.left is not None:
            return self.minimum_value(current_node.left)

        return current_node.data

    def maximum_value(self, current_node=None):
        """Szuka najwiekszej wartosci w drzewie

        Parameters
        ----------
        current_node : Node
            Aktualny node

        Returns
        -------
        number
            Zawartosc najwiekszego noda
        """

        if self.root is None:
            return None

        if current_node is None:
            current_node = self.root

        if current_node.right is not None:
            return self.maximum_value(current_node.right)

        return current_node.data

    def find(self, data):
        """Sprawdza czy podana liczba lub Node znjaduje sie w drzewie

        Parameters
        ----------
        data
            Wartosc lub node kotryu jest szukany

        Returns
        -------
        Node
            Noda jesli istnieje, None jesli nie istnieje
        """

        if type(data) != Node:
            data = Node(data)

        if self.root is None:
            return None
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
        bool, Node
            True oraz wskaznik do noda jesli istnieje, False oraz None jesli nie istnieje
        """

        if current_node is None:
            return current_node
        elif node.data == current_node.data:
            return current_node
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
        ValueError
            Jeśli podano bledny zakres

        Returns
        -------
        list
            Tablica liczb ktore dla podanego zakresu znajduja sie w drzewie
        """

        if x1 > x2:
            raise ValueError("Wrong scope")

        res = []
        if self.root is None:
            return res
        x_split = self.__find_x_split(self.root, x1, x2)
        if x_split.is_leaf():
            if x1 <= x_split.data <= x2:
                res.append(x_split.data)
        else:
            res.append(x_split.data)
            self.__range_searching_left(x_split.left, x1, res)
            self.__range_searching_right(x_split.right, x2, res)

        return res

    def __range_searching_left(self, current_node, x1, res):
        """Funkcja pomocnicza ktora dodaje do listy wszytkie nody znajdujace sie na lewo od Noda rozdzielajacego

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        x1 : int
            Poczatek zkaresu
        res : list
            Lista z elementami po lewej stronie od split noda
        """

        if x1 <= current_node.data:
            res.append(current_node.data)
            if current_node.left is not None:
                self.__range_searching_left(current_node.left, x1, res)
            if current_node.right is not None:
                self.__range_searching_left(current_node.right, x1, res)
        elif current_node.right is not None:
            self.__range_searching_left(current_node.right, x1, res)

    def __range_searching_right(self, current_node, x2, res):
        """Funkcja pomocnicza ktora dodaje do listy wszytkie nody znajdujace sie na prawo od Noda rozdzielajacego

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        x2 : int
            Koniec zkaresu
        res : list
            Lista z elementami po prawej stronie od split noda
        """

        if x2 >= current_node.data:
            res.append(current_node.data)
            if current_node.right is not None:
                self.__range_searching_right(current_node.right, x2, res)
            if current_node.left is not None:
                self.__range_searching_right(current_node.left, x2, res)
        elif current_node.left is not None:
            self.__range_searching_right(current_node.left, x2, res)

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

        """

        if self.root is None:
            return
        self.__print_tree_node(self.root)

    def __print_tree_node(self, current_node):
        """Funkcja pomocnicza wypiujaca zawartosc Noda

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        """

        if current_node.left:
            self.__print_tree_node(current_node.left)
        print(current_node.data)
        if current_node.right:
            self.__print_tree_node(current_node.right)

    def inorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci inorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci inorder
        """

        res = []
        if self.root is None:
            return res

        self.__inorder_traversal(self.root, res)
        return res

    def __inorder_traversal(self, current_node, res):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci inorder

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        res : list
            Lista ktora jest wypelniana elementami w kolejnosci inorder od current_node
        """

        if current_node:
            self.__inorder_traversal(current_node.left, res)
            res.append(current_node.data)
            self.__inorder_traversal(current_node.right, res)

    def preorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci preorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci preorder
        """

        res = []
        if self.root is None:
            return res

        self.__preorder_traversal(self.root, res)
        return res

    def __preorder_traversal(self, current_node, res):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci preorder

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        res : list
            Lista ktora jest wypelniana elementami w kolejnosci preorder od current_node
        """

        if current_node:
            res.append(current_node.data)
            self.__preorder_traversal(current_node.left, res)
            self.__preorder_traversal(current_node.right, res)

    def postorder_traversal(self):
        """Funkcja zwracajaca liste z zawartoscia Nodow w kolejnosci postorder

        Returns
        -------
        list
            Lista zawartosci Nodow w kolejnosci postorder
        """

        res = []
        if self.root is None:
            return res

        self.__postorder_traversal(self.root, res)
        return res

    def __postorder_traversal(self, current_node, res):
        """Funkcja pomocnicza przechodzaca przez drzewo w kolejnosci postorder

        Parameters
        ----------
        current_node : Node
            Node w ktorym sie aktualnie znajdujemy
        res : list
            Lista ktora jest wypelniana elementami w kolejnosci postorder od current_node
        """

        if current_node:
            self.__postorder_traversal(current_node.left, res)
            self.__postorder_traversal(current_node.right, res)
            res.append(current_node.data)
