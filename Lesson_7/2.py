"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
#http://py-algorithm.blogspot.com/2012/01/blog-post.html
import random

array = [random.random() * 50 for _ in range(20)]
[print(a) for a in array]


def MergerSort(a):
    def MergerGroup(a, left, m, right):
        if left >= right:
            return None
        if m < left or right < m:
            return None
        t = left
        for j in range(m + 1, right + 1):  # подгруппа 2
            for i in range(t, j):  # цикл подгруппы 1
                if a[j] < a[i]:
                    r = a[j]
                    # итерационно переставляем элементы, чтобы упорядочить
                    for k in range(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    t = i  # проджолжение вставки в группе 1
                    break  # к следующему узлу из подгруппы 2

    if len(a) < 2:
        return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):  # группы
            z = g + k + k - 1  # последний эл-т группы
            r = z if z < len(a) else len(a) - 1  # последняя группа
            MergerGroup(a, g, g + k - 1, r)  # слияние
            g += 2 * k
        k *= 2


MergerSort(array)
print('Отсортированный массив')
[print(a) for a in array]
