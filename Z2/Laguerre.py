import ast
import sys

from numpy import poly1d, polyder, sqrt

EPSILON = 0.0000000001


def laguerre(p, a, N):
    p = [float(val) for val in ast.literal_eval(p)]
    a = float(a)
    N = int(N)

    n = len(p) - 1

    dp = polyder(p)
    d2p = polyder(dp)

    pOf = poly1d(p)
    dpOf = poly1d(dp)
    d2pOf = poly1d(d2p)
    X_k = a

    k = 1
    while k < N and abs(pOf(X_k)) > EPSILON:
        if pOf(X_k) == 0:
            print("dzielenie przez zero!\nKonczenie pracy programu...")
            print(f"\nOstatni wyliczony po {k} iteracjach pierwiastek wielomianu {p} to:", "{:.10f}\n".format(float(X_k)))
            return X_k
        G = dpOf(X_k) / pOf(X_k)
        H = G ** 2 - d2pOf(X_k) / pOf(X_k)
        if (n - 1) * (n * H - G ** 2) >= 0:
            if abs(G + sqrt((n - 1) * (n * H - G ** 2))) > abs(G - sqrt((n - 1) * (n * H - G ** 2))):
                b = n / (G + ((n - 1) * (n * H - G ** 2)) ** (1 / 2))
            else:
                b = n / (G - ((n - 1) * (n * H - G ** 2)) ** (1 / 2))
        else:
            print("Liczba pod pierwiastkiem liczbą ujemną!\nKonczenie pracy programu...")
            print(f"\nOstatni wyliczony po {k} iteracjach potencjalny pierwiastek wielomianu {p} to:", "{:.10f}\n".format(float(X_k)))
            return X_k

        X_k = X_k - b
        k = k + 1

    print(f"\nWyliczony po {k} iteracjach pierwiastek wielomianu {p} to:", "{:.10f}\n".format(float(X_k)))
    return X_k


# przykladowe uzycie
# python Laguerre.py [1,2,3,-1] 1.5 10

# przykladowe uzycie (dzielenie przez ujemna wartosc pierwiastka) (Funkcja nie ma miejsc zerowych)
# python Laguerre.py [1,2,3] 2 10

# przykladowe uzycie (miejsca zerowe to 0 i 1.2711) - wartosc poczatkowa musi byc pomiedzy -0.96 a 3.35 aby metoda dzialala prawidlowo, inaczej metoda nie bedzie dzialac
# python Laguerre.py '[2, -4, 5, -4, 0]' -5 10
# python Laguerre.py '[2, -4, 5, -4, 0]' 3 10

# przykladowe uzycie 'prawidlowe' (miejsca zerowe to 0 i 1) - wartosc poczatkowa od 0.2 w góre obliczy miejsce zerowe '1', w p.p. '0'
# python Laguerre.py '[1, -4, 6, -4, 1, 0]' -50 10
# python Laguerre.py '[1, -4, 6, -4, 1, 0]' 5 10


# Ciekawy przyklad to python Laguerre.py [1,-2,3,-1] 2 10
# Poniewaz przy powyzszym punkcie poczatkowym '2' metoda 'wysypuje sie'
# Jednak przy punkcie poczatkowym mniejszym niz '1.13' i wiekszym niz '0.53' metoda dziala prawidlowo
# python Laguerre.py [1,-2,3,-1] 1 10


# przykladowe uzycie 
# python Laguerre.py [1,-5,6,1] -2 10

if len(sys.argv) > 1:
    laguerre(sys.argv[1], sys.argv[2], int(sys.argv[3]))
else:
    print("Prosze podac argumenty funkcji!\n\n"
          "Przykladowe wywolanie:\n"
          "python Laguerre.py [1,2,3] 2 10")