import string


def fun(line):
    word = ''.join([w for idx, w in enumerate(line) if idx == 0 or line[idx - 1] in string.whitespace])
    word2 = ''.join([w for idx, w in enumerate(line) if idx == len(line) - 1 or line[idx + 1] in string.whitespace])
    return word, word2


if __name__ == "__main__":
    print(fun("Ala ma kota"))
