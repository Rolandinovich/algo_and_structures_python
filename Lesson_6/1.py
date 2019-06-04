"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# python 3.7 , win 7 64. Все мои алгоритмы память не используют)))

from memory_profiler import profile
from random import randint
from math import inf
from math import trunc


@profile
def test_hypothesis(n, sum=1, cur_num=1):
    # если n=1 выходим
    if n == 1:
        print('Утверждение верно')
        return (1, {1: True})
    # последний шаг рекурсии
    if cur_num == n:
        # возвращаю значение n и словарь с результатом проверки
        # заполняю ниже
        return (n, {})
    # для каждого шага получаю сумму 1+2+...+n
    tail, result = test_hypothesis(n, sum + cur_num + 1, cur_num + 1)
    sum_left_side = sum + tail
    # проверяю
    if sum_left_side == (cur_num + 1) * (cur_num + 1 + 1) / 2:
        print(f'Гипотеза подтверждена для n={cur_num + 1}')
        # добавляю результат проверки в словарь
        result[cur_num + 1] = True
        if cur_num + 1 == 2:
            # если это последняя итерация возвращаю только результат
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


n = 10
print(test_hypothesis(n))


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     13     14.3 MiB     14.3 MiB   @profile
#     14                             def test_hypothesis(n, sum=1, cur_num=1):
#     15                                 # если n=1 выходим
#     16     14.3 MiB      0.0 MiB       if n == 1:
#     17                                     print('Утверждение верно')
#     18                                     return (1, {1: True})
#     19                                 # последний шаг рекурсии
#     20     14.3 MiB      0.0 MiB       if cur_num == n:
#     21                                     # возвращаю значение n и словарь с результатом проверки
#     22                                     # заполняю ниже
#     23     14.3 MiB      0.0 MiB           return (n, {})
#     24                                 # для каждого шага получаю сумму 1+2+...+n
#     25     14.3 MiB      0.0 MiB       tail, result = test_hypothesis(n, sum + cur_num + 1, cur_num + 1)
#     26     14.3 MiB      0.0 MiB       sum_left_side = sum + tail
#     27                                 # проверяю
#     28     14.3 MiB      0.0 MiB       if sum_left_side == (cur_num + 1) * (cur_num + 1 + 1) / 2:
#     29     14.3 MiB      0.0 MiB           print(f'Гипотеза подтверждена для n={cur_num + 1}')
#     30                                     # добавляю результат проверки в словарь
#     31     14.3 MiB      0.0 MiB           result[cur_num + 1] = True
#     32     14.3 MiB      0.0 MiB           if cur_num + 1 == 2:
#     33                                         # если это последняя итерация возвращаю только результат
#     34                                         return result
#     35                                     else:
#     36     14.3 MiB      0.0 MiB               return (cur_num, result)
#     37                                 else:
#     38                                     print(f'Гипотеза не верна для n={cur_num + 1}')
#     39                                     result[cur_num + 1] = False
#     40                                     if cur_num + 1 == 2:
#     41                                         return result
#     42                                     else:
#     43                                         return (cur_num, result)

@profile()
def max_in_min():
    N = 50
    MIN = -1000
    MAX = 1000
    matrix = []
    for _ in range(N):
        matrix_string = []
        for _ in range(N):
            matrix_string.append(randint(MIN, MAX))
        matrix.append(matrix_string)

    max_el = -inf
    for col_idx in range(N):
        min_el_in_col = inf
        for str_idx in range(N):
            if matrix[str_idx][col_idx] < min_el_in_col:
                min_el_in_col = matrix[str_idx][col_idx]
        if min_el_in_col > max_el:
            max_el = min_el_in_col


max_in_min()


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     86     14.6 MiB     14.6 MiB   @profile()
#     87                             def max_in_min():
#     88     14.6 MiB      0.0 MiB       N = 50
#     89     14.6 MiB      0.0 MiB       MIN = -1000
#     90     14.6 MiB      0.0 MiB       MAX = 1000
#     91     14.6 MiB      0.0 MiB       matrix = []
#     92     14.6 MiB      0.0 MiB       for _ in range(N):
#     93     14.6 MiB      0.0 MiB           matrix_string = []
#     94     14.6 MiB      0.0 MiB           for _ in range(N):
#     95     14.6 MiB      0.0 MiB               matrix_string.append(randint(MIN, MAX))
#     96     14.6 MiB      0.0 MiB           matrix.append(matrix_string)
#     97
#     98     14.6 MiB      0.0 MiB       max_el = -inf
#     99     14.6 MiB      0.0 MiB       for col_idx in range(N):
#    100     14.6 MiB      0.0 MiB           min_el_in_col = inf
#    101     14.6 MiB      0.0 MiB           for str_idx in range(N):
#    102     14.6 MiB      0.0 MiB               if matrix[str_idx][col_idx] < min_el_in_col:
#    103     14.6 MiB      0.0 MiB                   min_el_in_col = matrix[str_idx][col_idx]
#    104     14.6 MiB      0.0 MiB           if min_el_in_col > max_el:
#    105     14.6 MiB      0.0 MiB               max_el = min_el_in_col


@profile()
def revert(n):
    lastnum = n % 10
    new_n = n // 10
    if n // 10 == 0:
        return n
    return f'{str(lastnum)}{str(revert(new_n))}'


n = 651832
print(revert(n))

# Line #    Mem usage    Increment   Line Contents
# ================================================
#    139     14.7 MiB     14.7 MiB   @profile()
#    140                             def revert(n):
#    141     14.7 MiB      0.0 MiB       lastnum = n % 10
#    142     14.7 MiB      0.0 MiB       new_n = n // 10
#    143     14.7 MiB      0.0 MiB       if n // 10 == 0:
#    144     14.7 MiB      0.0 MiB           return n
#    145     14.7 MiB      0.0 MiB       return f'{str(lastnum)}{str(revert(new_n))}'