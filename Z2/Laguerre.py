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
    while k < N:
        if pOf(X_k) == 0:
            print("dzielenie przez zero!\nKonczenie pracy programu...")
            return X_k
        G = dpOf(X_k) / pOf(X_k)
        H = G ** 2 - d2pOf(X_k) / pOf(X_k)
        #  |G + sqrt((n - 1)*(nH - G^2))| > |G - sqrt((n - 1)*(nH - G^2))|
        if abs(G + ((n - 1) * (n * H - G ** 2))**(1/2)) > abs(G - ((n - 1) * (n * H - G ** 2))**(1/2)):
            b = n / (G + ((n - 1) * (n * H - G ** 2))**(1/2))
        else:
            b = n / (G - ((n - 1) * (n * H - G ** 2))**(1/2))

        X_k = X_k - b
        k = k + 1

    print(f"\nWyliczony po {k} iteracjach pierwiastek wielomianu {p} to: {X_k}")
    return X_k

# przykladowe uzycie (dzielenie przez 0):
# python Laguerre.py [1,2,3,-1] 1.5 10

# przykladowe uzycie (dzielenie przez ujemna wartosc pierwiastka)
# python Laguerre.py [1,2,3] 2 10

# przykladowe uzycie
#


laguerre(sys.argv[1], sys.argv[2], int(sys.argv[3]))

