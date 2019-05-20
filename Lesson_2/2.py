"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
from math import trunc


def go(n, count):
    lastnum = n % 10
    new_n = n // 10
    if lastnum % 2 == 0:
        count['chetnie'] += 1
    else:
        count['nechetnie'] += 1
    if new_n == 0:
        return count
    return go(new_n, count)


count = {'chetnie': 0, 'nechetnie': 0}
n = int(input('Введите натуральное число\n'))
print(go(n, count))
