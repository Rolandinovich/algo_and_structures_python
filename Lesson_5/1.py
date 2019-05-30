"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()
num = int(input('Введите количество предприятий: \n'))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия: \n')
    for j in range(QUARTERS):
        quarters.append((int(input(f'Прибыль за {j + 1}-й квартал: '))))
        profit += quarters[j]
    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit
average = total_profit / num
print(f'\n Средняя прибыль = {average}')
print(f'\n Предприятия с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Предприятие {comp.name} заработало {comp.profit}')

print(f'\n Предприятия с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profit < average:
        print(f'Предприятие {comp.name} заработало {comp.profit}')
