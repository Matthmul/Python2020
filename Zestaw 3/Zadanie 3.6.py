def fun(x, y):
    line = ''
    for k in range(y):
        for i in range(x):
            line += '+'
            for j in range(3):
                line += '-'
        line += '+\n'
        for i in range(x):
            line += '|'
            for j in range(3):
                line += ' '
        line += '|\n'
    for i in range(x):
        line += '+'
        for j in range(3):
            line += '-'
    line += '+\n'

    print(line)


if __name__ == "__main__":
    fun(5, 3)
