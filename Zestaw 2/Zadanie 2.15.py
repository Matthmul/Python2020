def fun(L):
    line = ''
    for number in L:
        line += str(number)
    return line


if __name__ == "__main__":
    print(fun([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
