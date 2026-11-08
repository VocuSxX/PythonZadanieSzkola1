import math
import random
from collections import Counter
import numpy as np

def szachownica(n):
    i, j = np.indices((n, n))
    return (i + j) % 2


def dodaj_na_koniec(tablica, wartosci):
    return np.append(tablica, wartosci)


def fahrenheit_na_celsjusz(f):
    f = np.array(f, dtype=float)
    return np.round((f - 32) * 5 / 9, 2)


def macierz_diagonalna(wartosci):
    wartosci = np.array(wartosci)
    if np.any(wartosci == 0):
        raise ValueError("Wartości na przekątnej muszą być niezerowe")
    return np.diag(wartosci)


def losowe_permutacje(lista, ile):
    max_perm = math.factorial(len(lista)) // math.prod(
        math.factorial(c) for c in Counter(lista).values()
    )
    if ile > max_perm:
        raise ValueError(f"Istnieje tylko {max_perm} różnych permutacji")
    wynik = set()
    while len(wynik) < ile:
        wynik.add(tuple(random.sample(lista, len(lista))))
    return list(wynik)


def odwroc_i_splaszcz(macierz):
    return np.array(macierz).flatten()[::-1]


def wektor_na_macierz(wektor, wiersze=None, kolumny=None):
    wektor = np.array(wektor)
    if wiersze is None and kolumny is None:
        return wektor.reshape(-1, 1)
    return wektor.reshape(wiersze if wiersze else -1, kolumny if kolumny else -1)


def iloczyn_skalarny(a, b):
    return np.dot(a, b)


def podmien_elementy(macierz, warunek, nowa_wartosc):
    macierz = np.array(macierz)
    return np.where(warunek(macierz), nowa_wartosc, macierz)


def te_same_indeksy(a, b):
    return np.where(np.array(a) == np.array(b))[0]


def macierz_z_wyznacznikiem(n, wyznacznik, minimum=-10, maksimum=10, max_prob=200000):
    for _ in range(max_prob):
        L = np.tril(np.random.randint(-2, 3, (n, n)), -1) + np.eye(n, dtype=int)
        U = np.triu(np.random.randint(-2, 3, (n, n)), 1)
        przekatna = np.ones(n, dtype=int)
        przekatna[0] = wyznacznik
        U = U + np.diag(przekatna)
        A = L @ U
        if A.min() >= minimum and A.max() <= maksimum:
            return A
    raise ValueError("Nie udało się znaleźć macierzy w podanym zakresie")

print("1. Napisz funkcję, która wygeneruje szachownicę złożoną z 0 i 1 o podanym rozmiarze.")
print(szachownica(6))

print("\n2. Napisz funkcję, która doda określone wartości na końcu macierzy. Przykładowe dane wejściowe [10,20,30], dane po rozszerzeniu [10,20,30,40,50,60,70,80,90].")
wejscie = [10, 20, 30]
print("Przed:", wejscie)
print("Po:   ", dodaj_na_koniec(wejscie, [40, 50, 60, 70, 80, 90]))

print("\n3. Stwórz funkcję, która przeliczy temperaturę ze stopni Farenheita na stopnie Celcjusza. Przykładowe dane wejściowe [0,12,45.21,34,99.91].")
dane_f = [0, 12, 45.21, 34, 99.91]
print("Fahrenheit:", dane_f)
print("Celsjusz:  ", fahrenheit_na_celsjusz(dane_f))

print("\n4. Napisz funkcję, która stworzy macierz z niezerowymi wartościami na przekątnej i zerami w pozostałych komórkach.  ")
print(macierz_diagonalna([3, 7, 1, 9]))

print("\n5. Napisz funckję, która dla danej listy z wartościami numerycznymi zwróci listę z zadaną ilością krotek, które będą różnymi permutacjami listy (przestawione w losowy sposób elementy w liście).")
for p in losowe_permutacje([1, 2, 3, 4], 5):
    print(p)

print("\n6. Napisz funkcję, która dla danych typu [[1,2,3],[4,5,6],[7,8,9]] zwróci wynik [9,8,7,6,5,4,3,2,1].")
print(odwroc_i_splaszcz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print("\n7. Napisz funkcję, która zamieni wektor na macierz dwuwymiarową.")
v = [1, 2, 3, 4, 5, 6]
print("Macierz-kolumna:\n", wektor_na_macierz(v))
print("Kształt 2x3:\n", wektor_na_macierz(v, 2, 3))

print("\n8. Napisz funkcję, która zwróci iloczyn skalarny dwóch wektorów.")
print(iloczyn_skalarny([1, 2, 3], [4, 5, 6]))  # 1*4 + 2*5 + 3*6 = 32

print("\n9. Napisz funkcję, która dla zadanej macierzy podmieni elementy spełniające zadany warunek (np. konkretną wartość na inną).")
m = np.array([[1, 2, 3], [4, 2, 6], [2, 8, 9]])
print("Przed:\n", m)
print("Po (2 -> 0):\n", podmien_elementy(m, lambda x: x == 2, 0))
print("Po (elementy > 5 -> -1):\n", podmien_elementy(m, lambda x: x > 5, -1))

print("\n10. Napisz fubkcję, która dla dwóch wektorów zwróci indeksy, które zawieraja te same wartości. Można skorzystać z metody np.where()")
print(te_same_indeksy([1, 2, 3, 4, 5], [1, 0, 3, 0, 5]))

print("\n11. Z Macierzy o rozmiarze 10x10, której elementy to kolejne liczby naturalne wybierz te elementy, które są podzielne przez 2 i nie są podzielne przez 3. Rozwiązanie uzyskaj za pomocą maskowania.")
M = np.arange(1, 101).reshape(10, 10)
maska = (M % 2 == 0) & (M % 3 != 0)
print(M[maska])

print("\n12. Z losowej macierzy o elementach z Z10 wybierz elementy, które są większe od średniej arytmetycznej elementów macierzy.")
Z = np.random.randint(0, 10, (5, 5))
print(Z)
print("Średnia:", Z.mean())
print(Z[Z > Z.mean()])

print("\n13. Napisz funkcję, która wygeneruje macierz o losowych elementach (liczby całkowite z zadanego zakresu) o zadanej z góry wartości wyznacznika.")
A = macierz_z_wyznacznikiem(3, 5, minimum=-10, maksimum=10)
print(A)
print("Wyznacznik:", round(np.linalg.det(A)))