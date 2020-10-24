def fun(lengt):
    line = ''
    for i in range(lengt):
        line += '|'
        for j in range(4):
            line += '.'

    line += '|\n'
    for i in range(lengt + 1):
        line += str(i)
        num_of_space = 5 - len(str(i + 1))
        line += " " * num_of_space
    print(line)


if __name__ == "__main__":
    fun(1000)
