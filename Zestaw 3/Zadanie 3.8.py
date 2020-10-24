from collections import Counter


def fun(sen1, sen2):
    lista1 = Counter(sen1)
    lista2 = Counter(sen2)

    listaa = lista1 & lista2
    listaa = set(listaa.elements())
    print(''.join(listaa))

    listab = lista1 | lista2
    listab = set(listab.elements())
    print(''.join(listab))


if __name__ == "__main__":
    fun("Ala ma kota", "Pies ma Krzysia")
