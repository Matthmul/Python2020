from random import seed
from random import random


def fun(L):
    line = ""
    for number in L:
        line += str(number).zfill(3) + " "
    return line


if __name__ == "__main__":
    seed(1)
    array = [int(1 + (i * (99 - 1)) * random()) for i in range(10)]
    print(array)
    print(fun(array))
