def fun3_5(lengt):
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
    return line


def fun3_6(x, y):
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
    return line


if __name__ == "__main__":
    print(fun3_5(1000))
    print(fun3_6(5, 3))
