import string


def fun(line):
    number = len([l for l in line if l not in string.whitespace])
    return number


if __name__ == "__main__":
    print(fun("Ala ma kota"))
