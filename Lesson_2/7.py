"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def test_hypothesis(n, sum=1, cur_num=1):
    if n == 1:
        return print('Утверждение верно')
    if cur_num == n:
        return n
    sum_left_side = sum + test_hypothesis(n, sum + cur_num + 1, cur_num + 1)
    if sum_left_side == (cur_num + 1) * (cur_num + 1 + 1) / 2:
        print(f'Гипотеза подтверждена для n={cur_num + 1}')
        return cur_num
    else:
        print(f'Гипотеза не верна для n={cur_num + 1}')
        return cur_num


n = int(input('Введите натуральное n\n'))
test_hypothesis(n)
