# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
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

mass[max_i], mass[min_i] = mass[min_i], mass[max_i]
