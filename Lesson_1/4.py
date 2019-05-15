"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random
from math import floor, trunc


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


s1, s2 = input('Введите границы числового( больше или равно 0) или буквенного диапазона:\n').split(' ')
if isfloat(s1) and isfloat(s2):
    if float(s1) < float(s2):
        left = float(s1)
        right = float(s2)
    else:
        left = float(s2)
        right = float(s1)
    print(f'Границы от {left} до {right}')
    if abs(right - left) < 1:
        print('целых чисел в диапазоне нет')
    else:
        if left < 0:
            left_int = trunc(left)
        else:
            left_int = trunc(left) + 1
        if right < 0:
            right_int = trunc(right)
        else:
            right_int = floor(right)
        print(f'Случайный целое число из заданного диапазона: {random.randint(left_int, floor(right))}')
    print(f'Случайный вещественное число из заданного диапазона: {random.uniform(left, right)}')
else:
    if s1 < s2:
        left = s1
        right = s2
    else:
        left = s2
        right = s1
    print(f'Границы от {left} до {right}')
    print(f'Случайный символ из заданного диапазона: {chr(random.randint(ord(left), ord(right)))}')
