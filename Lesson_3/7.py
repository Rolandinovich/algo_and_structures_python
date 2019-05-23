"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

from math import inf

mass = []
for _ in range(0, 200):
    mass.append(randint(-100, 100))

first_min = inf
for el in sorted(mass, reverse=True):
    if el <= first_min:
        second_min = first_min
        first_min = el
print(f'Минимальное число {first_min}, следующее минимальное {second_min}')
