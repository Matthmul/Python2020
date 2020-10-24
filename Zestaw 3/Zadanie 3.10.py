slownik = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman2int(word):
    number = 0
    for i in range(len(word)):
        if i == 0 or slownik[word[-i]] <= slownik[word[-i - 1]]:
            number += slownik[word[-i - 1]]
        else:
            number -= slownik[word[-i - 1]]
    return number


if __name__ == "__main__":
    assert 9 == roman2int("IX")
    assert 2020 == roman2int("MMXX")
    assert 999 == roman2int("CMXCIX")
    assert 1000 == roman2int("M")
    assert 444 == roman2int("CDXLIV")
    assert 1234 == roman2int("MCCXXXIV")
