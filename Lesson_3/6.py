"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

mass = []
for _ in range(0, 200):
    mass.append(randint(-100, 100))
# получаем первый по списку минимальный и максимальный эллемент в массиве
max_i = len(mass) - 1
min_i = max_i
for i in range(0, 199)[::-1]:
    if mass[i] <= mass[min_i]:
        min_i = i
    if mass[i] >= mass[max_i]:
        max_i = i

summ = 0
for i, el in enumerate(mass):
    if (min_i < i < max_i and min_i < max_i) or (min_i > i > max_i and min_i > max_i):
        summ += el
print(summ)
