# Подсчёт суммы цифр в строке

import sys

line = sys.argv[1]

sum_ = sum([int(i) for i in line])
print(sum_)
