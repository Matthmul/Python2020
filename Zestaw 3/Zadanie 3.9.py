def fun(lista):
    lista_out = [sum(l) for l in lista]

    print(lista_out)


if __name__ == "__main__":
    fun([[], [4], (1, 2), [3, 4], (5, 6, 7)])
