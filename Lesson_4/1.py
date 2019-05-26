"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit

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

cProfile.run('')
