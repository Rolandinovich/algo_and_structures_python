"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof


class SuperCar:
    def __init__(self):
        self.speed = 500
        self.consumption = 3, 1
        self.up_to_hundred = 5
        self.weight = 2000
        self.name = 'supercar'


class SuperCarLight:
    __slots__ = ['speed', 'consumption', 'up_to_hundred', 'weight', 'name']

    def __init__(self):
        self.speed = 500
        self.consumption = 3, 1
        self.up_to_hundred = 5
        self.weight = 2000
        self.name = 'supercar'


car1 = SuperCar()
car2 = SuperCarLight()
print('---car1---')
print(car1.__dict__)
print(asizeof.asizeof(car1))
print('---car2---')
print(car2.__slots__)
print(asizeof.asizeof(car2))
# ---car1---
# {'speed': 500, 'consumption': (3, 1), 'up_to_hundred': 5, 'weight': 2000, 'name': 'supercar'}
# 440
# ---car2---
# ['speed', 'consumption', 'up_to_hundred', 'weight', 'name']
# 208