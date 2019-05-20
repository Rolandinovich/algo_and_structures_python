"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def max_sum():
    def get_sum(number):
        new_number = number // 10
        if new_number == 0:
            return number
        last_num = number % 10
        return last_num + get_sum(new_number)

    number = input('Введите натуральное число. Для получения результата просто нажмите Enter\n')
    if number == '':
        return (0, 0)
    number = int(number)
    sum_number = get_sum(number)
    number_next_step, summ_next_step = max_sum()

    if sum_number > summ_next_step:
        return (number, sum_number)
    else:
        return (number_next_step, summ_next_step)


print(max_sum())
