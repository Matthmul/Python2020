def sum_seq(sequence):
    summ = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            summ = summ + sum_seq(x)
        else:
            summ = summ + x
    return summ


if __name__ == "__main__":
    assert sum_seq([0, 1, 2, 3, 4]) == 10
    assert sum_seq([0, [1, 2], 3, 4]) == 10
    assert sum_seq([0, [1, 2], [3, (4, 5)]]) == 15
