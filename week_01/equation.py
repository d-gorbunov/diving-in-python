# Решение квадратного уравнения

import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
    print('Корней нет')
    sys.exit(0)

d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Корней нет')
elif d == 0:
    x = int(-b / (2 * a))
    print(x)
else:
    x1 = int((-b + math.sqrt(d)) / (2 * a))
    x2 = int((-b - math.sqrt(d)) / (2 * a))
    print(x1, x2, sep='\n')
