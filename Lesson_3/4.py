# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint

mass = []
for _ in range(0, 200):
    mass.append(randint(-10, 10))

more_count_number = 0
for i in range(21):
    count = 0
    for el in mass:
        if el == i - 10:
            count += 1
    if count > more_count_number:
        more_count_number = count
        result_number = i - 10
print(f'Число {result_number} встречается {more_count_number} раз')
