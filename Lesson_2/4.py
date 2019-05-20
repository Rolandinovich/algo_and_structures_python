"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def range_sum(n, num=1):
    print(f'n={n}, num={num}')
    if n == 1:
        return num
    return num + range_sum(n - 1, -num / 2)


n = int(input('Введите n\n'))
print(range_sum(n))
