# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

from math import inf

N = 50
MIN = -1000
MAX = 1000
matrix = []
for _ in range(N):
    matrix_string = []
    for _ in range(N):
        matrix_string.append(randint(MIN, MAX))
    matrix.append(matrix_string)

max_el = -inf
for col_idx in range(N):
    min_el_in_col = inf
    for str_idx in range(N):
        if matrix[str_idx][col_idx] < min_el_in_col:
            min_el_in_col = matrix[str_idx][col_idx]
    if min_el_in_col > max_el:
        max_el = min_el_in_col

print(max_el)
