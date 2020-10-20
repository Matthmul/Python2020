def fun(line):
    words = line.split()
    alphabetic = sorted(words, key=str.lower)
    length = sorted(words, key=len)
    return " ".join(alphabetic), " ".join(length)


if __name__ == "__main__":
    print(fun("Ala ma kota"))
