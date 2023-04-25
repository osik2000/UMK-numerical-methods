import math

EPSILON = 0.000001


def falsi(a, b, function, N):
    if N <= 0:
        print("[Falsi]: N powinno byc wieksze od 0.")
        return
    if function(a) * function(b) > 0.0:
        print(
            "[Falsi]: "
            "Wartosci funkcji na krancach przedzialow nie sa liczbami o przeciwnych znakach - popraw przedzial!"
        )
    else:
        step = 1
        condition = True
        while condition and step <= N:
            x2 = a - (b - a) * function(a) / (function(b) - function(a))
            # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, function(x2)))

            if function(a) * function(x2) < 0:
                b = x2
            else:
                a = x2

            step = step + 1
            condition = abs(function(x2)) > EPSILON

        print(f"[Falsi]: Pierwiastek funkcji w tym przedziale to x = {x2:.10f}.")
        if step != 0:
            step = step - 1
        print(f"[Falsi]: Znaleziono go po {step} iteracjach.")
        return x2


# EXAMPLE FUNCTIONS

# 'dobry' przyklad
def function_1(x):
    return math.sin(x)


n = 100

a_1 = -2
b_1 = 3

print("\n[Falsi]: sin(x)")
falsi(float(a_1), float(b_1), function_1, n)


# 'dobry' przyklad
def function_2(x):
    return (math.e ** -x) * (3.2 * math.sin(x) - 0.5 * math.cos(x))


a_2 = 3
b_2 = 4

print("\n[Falsi]: Funkcja: e^-x * (3,2*sin(x) - 0,5*cos(x))")
falsi(float(a_2), float(b_2), function_2, n)


# 'niewygodny' przyklad:
def function_3(x):
    return x ** 3 - x ** 2 + 2


a_3 = -200
b_3 = 300
print("\n[Falsi]: x^3 - x^2 + 2")
falsi(float(a_3), float(b_3), function_3, n)  # droga do znalezienia dokladnego pierwiastka to 273463 iteracji
