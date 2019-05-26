"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit
from random import randint

n = 100


# timeit
# рекурсия
def test_hypothesis(n, sum=1, cur_num=1):
    if n == 1:
        print('Утверждение верно')
        return (1, {1: True})
    if cur_num == n:
        return (n, {})
    tail, result = test_hypothesis(n, sum + cur_num + 1, cur_num + 1)
    sum_left_side = sum + tail
    if sum_left_side == (cur_num + 1) * (cur_num + 1 + 1) / 2:
        print(f'Гипотеза подтверждена для n={cur_num + 1}')
        result[cur_num + 1] = True
        if cur_num + 1 == 2:
            return result
        else:
            return (cur_num, result)
    else:
        print(f'Гипотеза не верна для n={cur_num + 1}')
        result[cur_num + 1] = False
        if cur_num + 1 == 2:
            return result
        else:
            return (cur_num, result)


print(timeit.timeit("test_hypothesis(n)", setup="from __main__ import test_hypothesis; n=100", number=100))


#    0.11423819999999998
# цикл
def test_hypothesis_in_for(n):
    result = {}
    sum = 1
    for i in range(2, n + 1):
        sum += i
        result[i] = {sum == n * (n + 1) / 2}
    return result


print(
    timeit.timeit("test_hypothesis_in_for(n)", setup="from __main__ import test_hypothesis_in_for; n=100", number=100))


#   0.004665299999999983

# cProfile
def max_sum():
    def get_sum(number):
        new_number = number // 10
        if new_number == 0:
            return number
        last_num = number % 10
        return last_num + get_sum(new_number)

    number = randint(-1, 100)  # input('Введите натуральное число. Для получения результата просто нажмите Enter\n')
    if number == -1:
        return (0, 0)
    number = int(number)
    sum_number = get_sum(number)
    number_next_step, summ_next_step = max_sum()

    if sum_number > summ_next_step:
        return (number, sum_number)
    else:
        return (number_next_step, summ_next_step)


cProfile.run('max_sum()')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     102/1    0.000    0.000    0.000    0.000 1.py:58(max_sum)
#   190/101    0.000    0.000    0.000    0.000 1.py:59(get_sum)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       102    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       102    0.000    0.000    0.000    0.000 random.py:218(randint)
#       102    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       102    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       124    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
