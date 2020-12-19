from random import randint


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):  # zwraca losowy element
        if self.is_empty():
            raise ValueError("Queue is empty")
        rand = randint(0, len(self.items) - 1)
        item = self.items[rand]
        self.items[rand] = self.items[len(self.items) - 1]
        self.items.pop()

        return item

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):  # czyszczenie listy
        self.items = []


import unittest


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()
        self.items_in_queue = []

    def test_insert_remove(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.insert(1)
        self.items_in_queue.append(1)
        self.assertFalse(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())
        for x in range(2, 6):
            self.queue.insert(x)
            self.items_in_queue.append(x)

        item = self.queue.remove()
        self.assertIn(item, self.items_in_queue)
        self.items_in_queue.remove(item)
        self.assertFalse(self.queue.is_full())
        self.assertFalse(self.queue.is_empty())

        for x in range(2, 6):
            item = self.queue.remove()
            self.assertIn(item, self.items_in_queue)
            self.items_in_queue.remove(item)

        self.assertTrue(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())

        try:
            self.queue.remove()
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
