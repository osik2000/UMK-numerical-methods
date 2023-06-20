from scipy.integrate import quad
from math import sin, pi, exp


# przyklady:
#
# |   f(x): x ** 2          |   a = -2    |   b = 2      |    ile_prostokatow = 10
# |   f(x): sin(x)          |   a = 0     |   b = 2 * pi |    ile_prostokatow = 10 lub inna liczba
# |   f(x): exp(x)          |   a = 0     |   b = 2      |    ile_prostokatow = 100
# |   f(x): abs(x-1)        |   a = 0     |   b = 2      |    ile_prostokatow = (parzysta liczba - duza dokladnosc)

def f(x):
    return exp(x)


a = 0
b = 2
ile_prostokatow = 2


def sprawdzenie(func, a, b):            # zapisy z dokumentacji f. quad: Compute a definite integral.
    return quad(func, a, b)[0]          # Integrate func from a to b (possibly infinite interval)
                                        # using a technique from the Fortran library QUADPACK



def metoda_prostokatow(f, a, b, n):
    h = (b - a) / n  # Szerokość jednego prostokąta
    suma = 0
    for i in range(n):
        x = a + i * h  # Punkt graniczny prostokąta
        suma += f(x)  # Dodawanie wartości funkcji w punkcie granicznym
    wynik = suma * h  # Obliczenie sumy pól prostokątów
    return wynik


print("Metoda prostokatow:", metoda_prostokatow(f, a, b, ile_prostokatow))
print("Sprawdzenie metodą quad", sprawdzenie(f, a, b))
