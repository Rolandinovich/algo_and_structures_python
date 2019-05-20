"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def number_of_coincidences(n, number):
    if n == 0:
        return 0
    number_in_sequence = input('Введите число последовательности \n')
    if number_in_sequence == number:
        return 1 + number_of_coincidences(n - 1, number)
    else:
        return 0 + number_of_coincidences(n - 1, number)


n = int(input('Введите количество цифр в последовательности \n'))
number = input('Введите искомую цифру\n')
print(f'Искомых цифр {number_of_coincidences(n, number)}')
