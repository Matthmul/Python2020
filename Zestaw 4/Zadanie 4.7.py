def sum_seq(sequence):
    lista = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            lista = lista + sum_seq(x)
        else:
            lista.append(x)
    return lista


if __name__ == "__main__":
    assert sum_seq([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert sum_seq([0, [1, 2], 3, 4]) == [0, 1, 2, 3, 4]
    assert sum_seq([0, [1, 2], [3, (4, 5)]]) == [0, 1, 2, 3, 4, 5]
    assert sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
