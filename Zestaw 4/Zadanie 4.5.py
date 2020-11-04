def odwracanie_iter(L, left, right):
    for i, x in enumerate(range(left, int(right / 2 + right % 2) + len(L) % 2)):
        L[x], L[right - i] = L[right - i], L[x]
    return L


def odwracanie_rek(L, left, right):
    L[left], L[right] = L[right], L[left]
    if left + 1 <= right - 1:
        odwracanie_rek(L, left + 1, right - 1)
    return L


if __name__ == "__main__":
    assert odwracanie_iter([0, 1, 2, 3, 4], 1, 2) == [0, 2, 1, 3, 4]
    assert odwracanie_iter([0, 1, 2, 3, 4], 2, 3) == [0, 1, 3, 2, 4]
    assert odwracanie_iter([0, 1, 2, 3, 4], 1, 4) == [0, 4, 3, 2, 1]
    assert odwracanie_iter([0, 1, 2, 3, 4], 0, 4) == [4, 3, 2, 1, 0]
    assert odwracanie_iter([0, 1, 2, 3, 4, 5], 0, 5) == [5, 4, 3, 2, 1, 0]
    assert odwracanie_iter([0, 1, 2, 3, 4, 5, 6], 0, 6) == [6, 5, 4, 3, 2, 1, 0]

    assert odwracanie_rek([0, 1, 2, 3, 4], 1, 2) == [0, 2, 1, 3, 4]
    assert odwracanie_rek([0, 1, 2, 3, 4], 2, 3) == [0, 1, 3, 2, 4]
    assert odwracanie_rek([0, 1, 2, 3, 4], 1, 4) == [0, 4, 3, 2, 1]
    assert odwracanie_rek([0, 1, 2, 3, 4], 0, 4) == [4, 3, 2, 1, 0]
    assert odwracanie_rek([0, 1, 2, 3, 4, 5], 0, 5) == [5, 4, 3, 2, 1, 0]
    assert odwracanie_rek([0, 1, 2, 3, 4, 5, 6], 0, 6) == [6, 5, 4, 3, 2, 1, 0]
