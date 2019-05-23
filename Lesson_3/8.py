"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
mass = []
for i in range(4):
    mass_string = []
    sum = 0
    for j in range(4):
        num = float(input(f'Введите {j+1}ый эллемент {i+1}ой строки \n'))
        sum += num
        mass_string.append(num)
    mass_string.append(sum)
    mass.append(mass_string)

for s in mass:
    for el in s:
        print(str(el).center(5), end='')
    print('')
