# Рисование лестницы из символов решётки

import sys

n_steps = int(sys.argv[1])  # Количество ступенек

for i in range(n_steps):
    n_spaces = n_steps - (i+1)
    n_sharps = n_steps - n_spaces
    print(' ' * n_spaces + '#' * n_sharps)
