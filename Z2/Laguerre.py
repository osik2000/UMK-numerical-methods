import ast
import sys

from numpy import poly1d, polyder, sqrt

EPSILON = 0.000001


def laguerre(p, a, N):
    p = [float(val) for val in ast.literal_eval(p)]
    a = float(a)
    N = int(N)

    n = len(p)

    dp = polyder(p)
    d2p = polyder(dp)

    pOf = poly1d(p)
    dpOf = poly1d(dp)
    d2pOf = poly1d(d2p)
    X_k = a

    k = 1
    while k < N and pOf(X_k) > EPSILON:
        if pOf(X_k) == 0:
            print("dzielenie przez zero!\nKonczenie pracy programu...")
            print(f"\nOstatni wyliczony po {k} iteracjach pierwiastek wielomianu {p} to: {X_k}")
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
            print(f"\nOstatni wyliczony po {k} iteracjach potencjalny pierwiastek wielomianu {p} to: {X_k}")
            return X_k

        X_k = X_k - b
        k = k + 1

    print(f"\nWyliczony po {k} iteracjach pierwiastek wielomianu {p} to: {X_k}")
    return X_k


# przykladowe uzycie (dzielenie przez 0) (Funkcja zwroci ostatnią wartość, która jest zbliżona do miejsca zerowego):
# python Laguerre.py [1,2,3,-1] 1.5 10

# przykladowe uzycie (dzielenie przez ujemna wartosc pierwiastka) (Funkcja nie ma miejsc zerowych)
# python Laguerre.py [1,2,3] 2 10

# przykladowe uzycie
#

if len(sys.argv) > 1:
    laguerre(sys.argv[1], sys.argv[2], int(sys.argv[3]))
else:
    print("Prosze podac argumenty funkcji!\n\n"
          "Przykladowe wywolanie:\n"
          "python Laguerre.py [1,2,3] 2 10")
