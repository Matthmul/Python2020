def fibonacci_rek(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rek(n - 1) + fibonacci_rek(n - 2)


def fibonacci_iter(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    else:
        x = 0
        y = 1
        for i in range(2, n):
            temp = x + y
            x = y
            y = temp
    return y


if __name__ == "__main__":
    assert fibonacci_rek(0) == -1
    assert fibonacci_rek(1) == 0
    assert fibonacci_rek(2) == 1
    assert fibonacci_rek(3) == 1
    assert fibonacci_rek(4) == 2
    assert fibonacci_rek(5) == 3
    assert fibonacci_rek(6) == 5
    assert fibonacci_rek(10) == 34

    assert fibonacci_iter(0) == -1
    assert fibonacci_iter(1) == 0
    assert fibonacci_iter(2) == 1
    assert fibonacci_iter(3) == 1
    assert fibonacci_iter(4) == 2
    assert fibonacci_iter(5) == 3
    assert fibonacci_iter(6) == 5
    assert fibonacci_iter(10) == 34
