x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
    # Kod jest podobny do C++,
    # w Pythonie nie potrzeba dodawac ';'
    # oraz '()' w instruckji warunkowej

for i in "qwerty":
    if ord(i) < 100: print (i)
    # Nie jest poprawna poniewaz,
    # nastepna instrukcja warunkowa musi byc w kolejnej linijce

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Kod się wykona tylko kolejna instrukcja tj print
# powinna byc w następnej linii
