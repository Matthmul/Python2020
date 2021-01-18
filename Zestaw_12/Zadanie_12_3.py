def mediana_sort(L, left, right):
    if left > right:
        return None

    L_new = L[left: right + 1]

    left = 0
    right = len(L_new) - 1

    L_new.sort()
    i = ((left + right) // 2)

    if len(L_new) % 2:
        return L_new[i]
    else:
        return (L_new[i] + L_new[i + 1]) / 2


import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        pass

    def test_binarne_rek(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        size = len(L)

        self.assertEqual(mediana_sort(L, 0, size - 1), 5.5)
        self.assertEqual(mediana_sort(L, 2, size - 1), 6.5)
        self.assertEqual(mediana_sort(L, 5, size - 1), 8)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
