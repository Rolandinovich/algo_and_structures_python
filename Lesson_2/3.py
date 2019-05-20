"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
from math import trunc


def revert(n):
    lastnum = n % 10
    new_n = n // 10
    if n // 10 == 0:
        return n
    return f'{str(lastnum)}{str(revert(new_n))}'


n = int(input('Введите натуральное число\n'))
print(revert(n))
