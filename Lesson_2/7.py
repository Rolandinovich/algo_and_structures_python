"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


# получилось не прозрачно
# делаю проверку для всех случаев <=n
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


n = int(input('Введите натуральное n\n'))
print(test_hypothesis(n))
