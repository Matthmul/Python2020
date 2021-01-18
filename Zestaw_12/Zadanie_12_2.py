def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left > right:
        return None
    k = (left + right) // 2
    if y == L[k]:
        return k
    if y > L[k]:
        left = k + 1
    else:
        right = k - 1
    return binarne_rek(L, left, right, y)


import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        pass

    def test_binarne_rek(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        L.sort()
        size = len(L)

        self.assertEqual(binarne_rek(L, 0, size - 1, 3), 2)
        self.assertEqual(binarne_rek(L, 0, size - 1, 10), 9)
        self.assertEqual(binarne_rek(L, 0, size - 1, 1), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
