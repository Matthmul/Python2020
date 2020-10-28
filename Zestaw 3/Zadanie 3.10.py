slownik1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
slownik2 = dict(I=1,
                V=5,
                X=10,
                L=50,
                C=100,
                D=500,
                M=1000)

listofroman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
listofint = [1, 5, 10, 50, 100, 500, 1000]

slownik3 = dict(zip(listofroman, listofint))


def roman2int(word, dict):
    number = 0
    for i in range(len(word)):
        if i == 0 or dict[word[-i]] <= dict[word[-i - 1]]:
            number += dict[word[-i - 1]]
        else:
            number -= dict[word[-i - 1]]
    return number


if __name__ == "__main__":
    assert 9 == roman2int("IX", slownik1)
    assert 2020 == roman2int("MMXX", slownik1)
    assert 999 == roman2int("CMXCIX", slownik1)
    assert 1000 == roman2int("M", slownik1)
    assert 444 == roman2int("CDXLIV", slownik1)
    assert 1234 == roman2int("MCCXXXIV", slownik1)
    assert 9 == roman2int("IX", slownik2)
    assert 2020 == roman2int("MMXX", slownik2)
    assert 999 == roman2int("CMXCIX", slownik2)
    assert 1000 == roman2int("M", slownik2)
    assert 444 == roman2int("CDXLIV", slownik2)
    assert 1234 == roman2int("MCCXXXIV", slownik2)
    assert 9 == roman2int("IX", slownik3)
    assert 2020 == roman2int("MMXX", slownik3)
    assert 999 == roman2int("CMXCIX", slownik3)
    assert 1000 == roman2int("M", slownik3)
    assert 444 == roman2int("CDXLIV", slownik3)
    assert 1234 == roman2int("MCCXXXIV", slownik3)
