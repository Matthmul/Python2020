# Projekt Język Python: "Range Tree"

Projekt jest implementacją range tree dla liczb calkowitych.
Umozliwia przechowywanie duplikatow.

## Funkcje
* Przechowywanie danych w postaci liczb calkowitych 
* Sprawdzanie wystepowania danej liczby w drzewie
* Dodawanie oraz usuwanie liczb
* Przeszukiwanie drzewa i wypisywanie tablicy liczb ktore wystepuja w drzewie z podanego zakresu

## Opis funkcji
```python
def insert(data)
```

Dadanie podanej liczby do drzewa

```python
def delete(data)
```

Usuniecie podanej liczby do drzewa

```python
def minimum_value(current_node)
```

Wyszukanie najmniejszej wartosci w drzewie

```python
def maximum_value(current_node)
```

Wyszukanie najwiekszej wartosci w drzewie

```python
def find(data)
```

Sprawdzenie czy istnieje dana liczba w drzewie

```python
def range_searching(x1, x2)
```

Przeszukanie i zwrocenie liczb w drzewie z podanego zakresu

```python
def print_tree()
```

Wypisanie drzewa w kolejnosci inorder

```python
def inorder_traversal()
```

Zwrocenie tablicy z elementami drzewa w kolejnosci inorder

```python
def preorder_traversal()
```

Zwrocenie tablicy z elementami drzewa w kolejnosci preorder

```python
def postorder_traversal()
```

Zwrocenie tablicy z elementami drzewa w kolejnosci postorder

## Implementacja
Po sklonowaniu repozytorium

```python
from Projekt.range_tree import RangeTree

rangetree = RangeTree()
```

## Zrodla

[Range tree wikipedia](https://en.wikipedia.org/wiki/Range_tree)

[Prezentacja 1](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/rangetrees.pdf)

[Prezentacja 2](https://www.bowdoin.edu/~ltoma/teaching/cs3250-CompGeom/spring16/Lectures/cg-rangetrees.pdf)

## Autor
Maciej Mularski

## Python Version
Python 3