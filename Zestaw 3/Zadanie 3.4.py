import re


def potega(x):
    return pow(x, 3)


def xx():
    inp = ''
    while inp != "stop":
        inp = input("Podaj liczbe: ")
        if inp == "stop":
            continue
        if re.match(r'^-?\d+(?:\.\d+)?$', inp) is None:
            print("Nie podano liczby")
        else:
            inp = float(inp)
            print(inp, potega(inp))


if __name__ == "__main__":
    xx()
