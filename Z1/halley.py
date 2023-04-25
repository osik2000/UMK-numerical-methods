import math

EPSILON = 0.00001


def halley(x0, N, f, f_prime, f_double_prime):
    x = x0 if x0 != 0 else 0.0001
    i = 0
    if N <= 0:
        print("N powinno byc wieksze od 0.")
        return
    while i < N:
        fx = f(x)
        fx_prime = f_prime(x)
        fx_double_prime = f_double_prime(x)
        delta_x = (2 * fx * fx_prime) / (2 * fx_prime * fx_prime - fx * fx_double_prime)
        x -= delta_x
        if abs(delta_x) < EPSILON:
            print(f"[Halley]: Pierwiastek funkcji w tym przedziale to x = {x:.10f}.")
            print(f"[Halley]: Znaleziono go po {i} iteracjach.")
            return
        i += 1
    print(f"[Halley]: Po {N} iteracjach nie znaleziono pierwiastkow rownania.")


# EXAMPLE FUNCTIONS


def function_1(x):
    return math.sin(x)


def function_prime_1(x):
    return math.cos(x)


def function_double_prime_1(x):
    return -1 * math.sin(x)


n = 100
x0_1 = -1
print("\n[Halley]: Funkcja: sin(x)")
halley(x0_1, n, function_1, function_prime_1, function_double_prime_1)


# 'niewygodny' przyklad dla metody falsi okazal sie 'latwy' dla metody halley'a:
def function_2(x):
    return x ** 3 - x ** 2 + 2


def function_prime_2(x):
    return x * (3 * x - 2)


def function_double_prime_2(x):
    return 6 * x - 2


# Przyklad pokazujacy lepsze dzialanie dla tej funkcji niz w przypadku metody falsi
x0_2 = -200
print("\n[Halley]: Funkcja: x^3 - x^2 + 2")
halley(x0_2, n, function_2, function_prime_2,
       function_double_prime_2)


# 'niewygodny' przyklad:
def function_3(x):
    return 2 * x ** 3 - 2 * x - 5


def function_prime_3(x):
    return 6 * x ** 2 - 2


def function_double_prime_3(x):
    return 12 * x


# Przyklad pokazujacy lepsze dzialanie dla tej funkcji niz w przypadku metody falsi
x0_3 = 0
print("\n[Halley]: Funkcja: 2x^3 - 2x - 5")
halley(x0_3, n, function_3, function_prime_3,
       function_double_prime_3)  # droga do znalezienia dokladnego pierwiastka to 273463 iteracji
