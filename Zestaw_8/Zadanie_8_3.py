import math
from random import random


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    if n <= 0:
        return 0
    score = 0
    for i in range(n):
        x = random() ** 2
        y = random() ** 2
        if math.sqrt(x + y) <= 1:
            score += 1
    result = (score / n) * 4
    return result


if __name__ == '__main__':
    assert calc_pi(0) == 0
    assert calc_pi(-1) == 0
    print(calc_pi(10))
    print(calc_pi(100))
    print(calc_pi(1000))
    print(calc_pi(10000))
    print(calc_pi(100000))
    print(calc_pi(1000000))
    print(calc_pi(10000000))
    print(calc_pi(100000000))
