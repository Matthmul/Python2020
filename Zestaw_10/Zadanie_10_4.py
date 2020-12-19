class Queue:

    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None  # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_put_get(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(1)
        self.assertFalse(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())
        for x in range(2, 6):
            self.queue.put(x)
        self.assertTrue(self.queue.is_full())

        try:
            self.queue.put(7)
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

        self.assertEqual(1, self.queue.get())
        self.assertFalse(self.queue.is_full())
        self.assertFalse(self.queue.is_empty())

        for x in range(2, 6):
            self.assertEqual(x, self.queue.get())

        self.assertTrue(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())

        try:
            self.queue.get()
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
