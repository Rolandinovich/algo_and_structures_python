"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

array = [random.randint(-100, 100) for _ in range(20)]
print(array)


def bubble_sort(array):
    n = 1
    len_array = len(array)
    while n < len(array):
        for i in range(len_array - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                if len_array - 2 == i:
                    # в качестве улучшения перестаю сравнивать последние эллементы массива
                    # так как они уже на своём месте
                    len_array -= 1
        n += 1


bubble_sort(array)
print(array)
