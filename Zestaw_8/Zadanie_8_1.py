def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("x dowolny, y dowolny")
    elif a == 0 and b == 0:
        print("brak rozwiazan")
    elif a == 0:
        print("x dowolny, y = ", -c / b)
    elif b == 0:
        print("x = ", -c / a, ", y dowolny")
    else:
        print("x = (", -b, " * y - ", c, ") /", a, ", y = (", -a, " * x - ", c, ") /", b)


if __name__ == '__main__':
    solve1(0, 0, 0)
    solve1(0, 0, 1)
    solve1(0, 0, -1)
    solve1(0, 1, 0)
    solve1(0, 1, 1)
    solve1(1, 0, 0)
    solve1(1, 0, 1)
    solve1(1, 1, 1)
    solve1(1, -1, 1)
