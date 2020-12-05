import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        raise ValueError("Wrong values", a, b, c)


if __name__ == '__main__':
    try:
        print(heron(1, 1, 1))
        print(heron(3, 4, 5))
        print(heron(0, 1, 1))
    except Exception as e:
        print(e)
