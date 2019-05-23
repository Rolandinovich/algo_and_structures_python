# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

from math import inf

mass = []
for _ in range(0, 200):
    mass.append(randint(-100, 100))

max_negative_number = -inf
for i,el in enumerate(mass):
    if el > max_negative_number and el < 0:
        max_negative_number = el
        index = i

print(f'Максимальный отрицательный эллемент {max_negative_number} с начала списка имеет индекс {index} ')
