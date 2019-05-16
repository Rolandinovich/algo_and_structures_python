# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

num1, num2, num3 = input('Введите через пробел 3 разных числа:\n').split(' ')
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
if num2 < num1 > num3:
    if num2 > num3:
        print(f'Среднее число {num2}')
    else:
        print(f'Среднее число {num3}')
elif num2 < num1 < num3:
    print(f'Среднее число {num1}')
elif num2 > num1 < num3:
    if num2 > num3:
        print(f'Среднее число {num3}')
    else:
        print(f'Среднее число {num2}')
