L = [3, 5, 4] ; L = L.sort()
# Funkcja sort() nic nie zwraca

x, y = 1, 2, 3
# Do x i y moze byc przypisana 1 wartosc, pozostale 2 i 3 spowoduja
# blad interpretera

X = 1, 2, 3 ; X[1] = 4
# Zostanie przypisana 1 wrtosc pozostale zostana zignorowane,
# przez co nie powstanie tablica i nie mozna sie bedzie
# odwolac do 2 wartosci w niej,
# powstanie blad

X = [1, 2, 3] ; X[3] = 4
# Odwoluje sie do nieistniejacej wartosci w tablicy
# wyrzuci blad index out of range

X = "abc" ; X.append("d")
# String nie posiada wbudowanej funkcji append

L = list(map(pow, range(8)))
# Do dzialania funcja pow potrzebuje 2 argumentow aktualnie ma 1
