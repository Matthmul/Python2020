import time


# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def P_iter(i, j):
    if i < 0 or j < 0:
        return 0.0
    data = [[0 for _ in range(j + 1)] for _ in range(i + 1)]

    for a in range(i + 1):
        for b in range(j + 1):
            if a == 0 and b == 0:
                data[a][b] = 0.5
            elif a > 0 and b == 0:
                data[a][b] = 0.0
            elif a == 0 and b > 0:
                data[a][b] = 1.0
            else:
                data[a][b] = 0.5 * data[a - 1][b] + data[a][b - 1]
    return data[i][j]


def P_rec(i, j):
    if i < 0 or j < 0:
        return 0.0
    elif i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * P_rec(i - 1, j) + P_rec(i, j - 1)


if __name__ == '__main__':
    start = time.time()
    print(P_iter(0, 0))
    print(P_iter(1, 1))
    print(P_iter(0, 10))
    print(P_iter(10, 0))
    print(P_iter(10, 10))
    print(P_iter(100, 100))
    print(P_iter(1000, 1000))
    print(P_iter(3000, 0))
    stop = time.time()
    total_iter = stop - start

    start = time.time()
    print(P_rec(0, 0))
    print(P_rec(1, 1))
    print(P_rec(0, 10))
    print(P_rec(10, 0))
    print(P_iter(10, 10))
    print(P_iter(100, 100))
    print(P_iter(1000, 1000))
    print(P_iter(3000, 0))
    stop = time.time()
    total_rec = stop - start

    print("Iteration time", total_iter)
    print("Recursion time", total_rec)
