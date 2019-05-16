"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
segment_length1, segment_length2, segment_length3 = input('Введите через пробел 3 длины отрезков:\n').split(' ')
segment_length1 = float(segment_length1)
segment_length2 = float(segment_length2)
segment_length3 = float(segment_length3)
if (segment_length1 + segment_length2 <= segment_length3) or (
        segment_length1 + segment_length3 <= segment_length2) or (
        segment_length2 + segment_length3 <= segment_length1):
    print('Треугольник не существует')
else:
    print('Треугольник существует')
    if segment_length1 != segment_length2 and segment_length1 != segment_length3 and segment_length2 != segment_length3:
        print('Треугольник разносторонний')
    elif segment_length1 == segment_length2 == segment_length3:
        print('Треугольник равносторонний')
    else:
        print('Треугольник равнобедренный')
