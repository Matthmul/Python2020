import string


def fun(word):
    word_out = ""
    for w in word:
        word_out = word_out + w + "_"
    return word_out[:-1]


if __name__ == "__main__":
    print(fun("Ala"))
