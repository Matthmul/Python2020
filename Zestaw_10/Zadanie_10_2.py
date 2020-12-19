class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stack is full")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(5)

    def test_push_pop(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertFalse(self.stack.is_full())
        for x in range(2, 6):
            self.stack.push(x)
        self.assertTrue(self.stack.is_full())

        try:
            self.stack.push(7)
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

        self.assertEqual(5, self.stack.pop())
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.stack.is_empty())

        for x in range(4, 0, -1):
            self.assertEqual(x, self.stack.pop())

        self.assertTrue(self.stack.is_empty())
        self.assertFalse(self.stack.is_full())

        try:
            self.stack.pop()
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
