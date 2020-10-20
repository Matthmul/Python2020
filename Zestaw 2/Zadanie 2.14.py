def fun(line):
    maxsize = 0
    longest_word = ''
    for word in line.split():
        if len(word) > maxsize:
            maxsize = len(word)
            longest_word = word

    return longest_word, len(longest_word)


if __name__ == "__main__":
    print(fun("Ala ma kota"))
