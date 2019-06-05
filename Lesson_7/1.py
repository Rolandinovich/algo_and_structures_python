"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

array = [random.randint(-100, 99) for _ in range(20)]
print(array)


def bubble_sort(array):
    n = 1
    len_array = len(array)
    while n < len(array):
        is_sorted = True
        for i in range(len_array - 1):
            if array[i] < array[i + 1]:
                # если перестановок не было признак сортированного массива сохранится
                is_sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
                if len_array - 2 == i:
                    # в качестве улучшения перестаю сравнивать последние эллементы массива
                    # так как они уже на своём месте
                    len_array -= 1
        if is_sorted:
            break
        n += 1


bubble_sort(array)
print(array)
