import math


def solve2(a, b, c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("x dowolny")
        else:
            print("brak rozwiazan")
    elif a == 0:
        x = -c / b
        print("x = ", x)
    else:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
        elif delta == 0:
            x1 = -b / 2 * a
            x2 = x1
        else:
            x1 = complex(-b / (2 * a), - math.sqrt(-delta) / (2 * a))
            x2 = complex(-b / (2 * a), math.sqrt(-delta) / (2 * a))
        print("x1 = ", x1, ", x2 = ", x2)


if __name__ == '__main__':
    solve2(0, 0, 0)
    solve2(0, 0, 2)
    solve2(0, 2, 2)
    solve2(1, 0, -1)
    solve2(1, 1, 1)
    solve2(2, 2, 2)
    solve2(3, 2, 1)
    solve2(1, 2, 3)
    solve2(1, 3, 2)
