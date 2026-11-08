import math
import random

import numpy as np
import matplotlib.pyplot as plt


def wykres_sinus():
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(x)

    x_ekstrema = [np.pi / 2, 3 * np.pi / 2]
    y_ekstrema = [1, -1]

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, color="blue", label="y = sin(x)")
    plt.scatter(x_ekstrema, y_ekstrema, color="red", zorder=3, label="ekstrema (1 i -1)")

    plt.xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        ["0", "π/2", "π", "3π/2", "2π"],
    )
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.axhline(0, color="black", linewidth=0.8)
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1.2, 1.2)
    plt.title("Wykres funkcji sinus")
    plt.xlabel("x [rad]")
    plt.ylabel("sin(x)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper right")
    plt.show()


def wykres_scatter(n=100):
    x = np.random.randn(n)
    y = np.random.randn(n)
    kolory = np.random.rand(n)
    rozmiary = (30 * np.random.rand(n)) ** 2

    plt.figure(figsize=(6, 5))
    punkty = plt.scatter(x, y, c=kolory, s=rozmiary, cmap="hsv", alpha=0.8)
    plt.colorbar(punkty)
    plt.show()


def subploty_trygonometryczne():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    with np.errstate(divide="ignore", invalid="ignore"):
        tg = np.tan(x)
        ctg = 1 / np.tan(x)
    tg[np.abs(tg) > 10] = np.nan
    ctg[np.abs(ctg) > 10] = np.nan

    funkcje = [
        ("f(x) = sin(x)", np.sin(x), "blue"),
        ("f(x) = cos(x)", np.cos(x), "green"),
        ("f(x) = tg(x)", tg, "red"),
        ("f(x) = ctg(x)", ctg, "purple"),
    ]

    fig, osie = plt.subplots(2, 2, figsize=(10, 7))
    for ax, (tytul, y, kolor) in zip(osie.flat, funkcje):
        ax.plot(x, y, color=kolor)
        ax.set_title(tytul)
        ax.set_xlabel("x [rad]")
        ax.set_ylabel("f(x)")
        ax.axhline(0, color="black", linewidth=0.8)
        ax.grid(True, linestyle="--", alpha=0.6)
        if "tg" in tytul or "ctg" in tytul:
            ax.set_ylim(-10, 10)
    fig.suptitle("Funkcje trygonometryczne")
    fig.tight_layout()
    plt.show()


def wykres_ocen(dane):
    for przedmiot, oceny in dane.items():
        kolokwium = oceny["kolokwium"]
        egzamin = oceny["egzamin"]
        pozycje = np.arange(1, len(kolokwium) + 1)
        szerokosc = 0.4

        plt.figure(figsize=(7, 4))
        plt.bar(pozycje - szerokosc / 2, kolokwium, szerokosc, label="kolokwium")
        plt.bar(pozycje + szerokosc / 2, egzamin, szerokosc, label="egzamin")
        plt.xticks(pozycje)
        plt.xlabel("student")
        plt.ylabel("ocena")
        plt.legend()
        plt.show()


def monte_carlo_calka(n=1000):
    a, b = 0, np.pi
    wysokosc = 1
    x_los = np.random.uniform(a, b, n)
    y_los = np.random.uniform(0, wysokosc, n)

    pod_krzywa = y_los <= np.sin(x_los)
    pole_prostokata = (b - a) * wysokosc
    przyblizenie = pole_prostokata * pod_krzywa.sum() / n

    x = np.linspace(a, b, 500)
    plt.figure(figsize=(6, 4))
    plt.plot(x, np.sin(x), color="black")
    plt.scatter(x_los[pod_krzywa], y_los[pod_krzywa], color="red", s=4)
    plt.scatter(x_los[~pod_krzywa], y_los[~pod_krzywa], color="blue", s=4)
    plt.title("Pole pod funkcją sinx")
    plt.xlabel("x")
    plt.ylabel("sinx")
    plt.show()
    return przyblizenie


print("1. Napisz procedurę, która wyświetli wykres funkcji sinus z zaznaczonymi w postaci czerwonych punktów ekstremami (punkty 1 i -1 na osi rzędnych). Wykres powinien zawierać modyfikacje osi i odpowiednie podpisy oraz legendę.")
wykres_sinus()

print("\n2. Napisz procedurę, która za pomocą metody scatter() wyświetli wykres przedstawiający losowe dane. Wykorzystaj mapę kolorów za pomocą atrybutu cmap.")
wykres_scatter()

print("\n3. Napisz procedurę, która wyświetli subploty w układzie 2x2 z wartościami funkcji f(x)={sinx,cosx,tanx,cotx}. Podpisz wykresy i osie.")
subploty_trygonometryczne()

print("\n4. Napisz procedurę, która dla danych {'matematyka': {'kolokwium': [4, 5, 3.5], 'egzamin': [3.5, 5, 4]}} przedstawiających oceny 3 studentów z kolokwium i egzaminu z przedmiotu matematyka wyświetli wykres.")
dane = {'matematyka': {'kolokwium': [4, 5, 3.5], 'egzamin': [3.5, 5, 4]}}
wykres_ocen(dane)

print("\n5. Stwórz wykres, który przedstawi wizualizację obliczania przybliżonej wartości całki funkcji sinx na przedziale [0,π] za pomocą metody Monte-Carlo.")
wynik = monte_carlo_calka(1000)
print("Przybliżona wartość całki:", wynik, "(wartość dokładna: 2)")