from ast import literal_eval
from sys import argv

from numpy import roots, isreal, real

EPSILON = 0.0000000001
allRoots = False  # if true -> function my_roots will show all roots in complex form.


def my_roots(p):
    values = roots(p)
    roots_result = []
    if allRoots:
        for i in range(0, values.size):
            roots_result.append(values[i])
    else:
        for i in range(0, values.size):
            if isreal(values[i]):
                roots_result.append(real(values[i]))

    print(roots_result)


# # przykladowe uzycia (pierwiastki wielokrotne)
# python roots.py [1,8,28,56,70,56,28,8,1]
# python roots.py [1,6,15,20,15,6,1]
# python roots.py [-1,2,3,5]
# python roots.py [1,-6,12,-8]
# python compan_plus_eig.py '[1,2,-17,-4,31,2,-15]' # znajduje wszystkie niezaleznie od zmiennej
#
# # przykladowe uzycia (zwykle)
#
# python compan_plus_eig.py [1,-1,-23,37,41,-30,-40]
# python compan_plus_eig.py [-3,6,-4,1,0]
# python roots.py [1,2,-15,-34,24]


if len(argv) > 1:
    my_roots([float(val) for val in literal_eval(argv[1])])
else:
    print("Prosze podac argumenty funkcji!\n\n"
          "Przykladowe wywolanie:\n"
          "python roots.py [1,2,3]")
