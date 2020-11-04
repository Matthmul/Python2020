def factorial_rek(n):
    if n in (0, 1):
        return 1
    elif n > 1:
        return n * factorial_rek(n - 1)


def factorial_iter(n):
    tmp = 1
    if n in (0, 1):
        return 1
    else:
        for i in range(2, n + 1):
            tmp = tmp * i
    return tmp


if __name__ == "__main__":
    assert factorial_rek(0) == 1
    assert factorial_rek(1) == 1
    assert factorial_rek(2) == 2
    assert factorial_rek(4) == 24
    assert factorial_rek(10) == 3628800

    assert factorial_iter(0) == 1
    assert factorial_iter(1) == 1
    assert factorial_iter(2) == 2
    assert factorial_iter(4) == 24
    assert factorial_iter(10) == 3628800
