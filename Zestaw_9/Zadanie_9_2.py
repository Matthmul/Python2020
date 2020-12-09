class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):  # klasy O(N)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            while self.head.next.next:
                self.head = self.head.next
            self.head.next = None
            self.tail = self.head
        self.length -= 1
        return node

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):  # klasy O(1)
        if other.is_empty():
            raise ValueError("pusta lista")
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()

    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        self.length = 0
        self.head = None
        self.tail = None


import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.alist = SingleList()
        self.blist = SingleList()

    def test_insert_head(self):
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.blist.insert_head(Node(11))  # [11]
        self.blist.insert_head(Node(22))  # [22, 11]
        self.assertEqual(self.alist.count(), 2)
        self.assertEqual(self.blist.count(), 2)

    def test_insert_tail(self):
        self.alist.insert_tail(Node(33))  # [22, 11, 33]
        self.blist.insert_tail(Node(33))  # [22, 11, 33]

    def test_merge(self):
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.blist.insert_head(Node(11))  # [11]
        self.blist.insert_head(Node(22))  # [22, 11]
        self.alist.merge(self.blist)
        self.assertEqual(self.alist.count(), 4)
        self.assertEqual(self.blist.count(), 0)

    def test_remove_head(self):
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.alist.insert_tail(Node(33))  # [22, 11, 33]

        self.assertEqual(self.alist.count(), 3)
        self.assertEqual("{}".format(self.alist.remove_head()), "22")
        self.assertEqual(self.alist.count(), 2)

    def test_remove_tail(self):
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.alist.insert_tail(Node(33))  # [22, 11, 33]

        self.assertEqual(self.alist.count(), 3)
        self.assertEqual("{}".format(self.alist.remove_tail()), "33")
        self.assertEqual("{}".format(self.alist.remove_tail()), "11")
        self.assertEqual(self.alist.count(), 1)

    def test_clear(self):
        self.alist.insert_head(Node(11))  # [11]
        self.alist.insert_head(Node(22))  # [22, 11]
        self.alist.insert_tail(Node(33))  # [22, 11, 33]

        self.assertEqual(self.alist.count(), 3)
        self.alist.clear()  # [22, 11, 33]
        self.assertEqual(self.alist.count(), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
