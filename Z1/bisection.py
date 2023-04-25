import math

EPSILON = 0.000000001


def bisection(a, b, N, func):
    if N <= 0:
        print("[Bisection]: N powinno byc wieksze od 0.")
        return
    if func(a) * func(b) >= 0:
        print(
            "[Bisection]: "
            "Wartosci funkcji na krancach przedzialow nie sa liczbami o przeciwnych znakach - popraw przedzial!"
        )
        return
    c = a
    i = 0
    while (b - a) >= EPSILON and (i < N):
        c = (a + b) / 2
        if func(c) == 0.0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        i += 1
    print(f"[Bisection]: Pierwiastek funkcji w tym przedziale to x = {c:.10f}")
    if i != 0:
        i = i - 1
    print(f"[Bisection]: Znaleziono go po {i} iteracjach.")
    return c


# EXAMPLE FUNCTIONS


# 'latwy' przyklad
def function_1(x):
    return math.sin(x)


n = 100
a_1 = -1
b_1 = 2
print("\n[Bisection]: Funkcja: sin(x)")
bisection(a_1, b_1, n, function_1)


# 'niewygodny' przyklad
def function_2(x):
    return math.cos(x - 2)


a_2 = -3
b_2 = 5
print("\n[Bisection]: Funkcja: cos(x-2)")
bisection(a_2, b_2, n, function_2)


# 'niewygodny' przyklad
def function_3(x):
    return x**3 + 2 * x**2 + x - 1


a_3 = -1
b_3 = 3
print("\n[Bisection]: Funkcja: x^3 + 2x^2 + x - 1")
bisection(a_3, b_3, n, function_3)
