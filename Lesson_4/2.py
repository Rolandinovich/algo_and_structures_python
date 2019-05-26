"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

# индекс искомого числа в последовательности целых чисел
import timeit

idx = 30


# сложность O(N)
def find_simple_without_eratosfen(idx):
    simple_num_idx = 1
    brake_count = 0
    number_in_step = 2
    while True:
        if brake_count == 1000000:
            print('Выходим по границе работы алгоритма')
            return 0
        brake_count += 1
        is_simple = True
        for i in range(2, number_in_step):
            if number_in_step % i == 0:
                is_simple = False
        if is_simple and simple_num_idx == idx:
            return number_in_step
        elif is_simple:
            simple_num_idx += 1
            number_in_step += 1
        else:
            number_in_step += 1


print(find_simple_without_eratosfen(idx))

print(timeit.timeit("find_simple_without_eratosfen(idx)",
                    setup="from __main__ import find_simple_without_eratosfen; idx=50",
                    number=100))
# 0.16910000000000003

#
print(timeit.timeit("find_simple_without_eratosfen(idx)",
                    setup="from __main__ import find_simple_without_eratosfen; idx=200",
                    number=100))
# 5.510764500000008

# сложность O(1)
def find_simple_with_eratosfen(idx):
    # список заполняется значениями от 0 до n
    n = 1000000
    a = []
    for i in range(n + 1):
        a.append(i)

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    # начинаем с 3-го элемента
    i = 2
    while i <= n:
        # Если значение ячейки до этого не было обнулено,
        # в этой ячейке содержится простое число.
        if a[i] != 0:
            # первое кратное ему будет в два раза больше
            j = i + i
            while j <= n:
                # это число составное, поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу, которое кратно i (оно на i больше)
                j = j + i
        i += 1

    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)
    # удаляем ноль
    a.remove(0)
    a = sorted(list(a))
    if len(a) > idx:
        return a[idx]
    else:
        return 0


print(find_simple_with_eratosfen(idx - 1))



print(timeit.timeit("find_simple_with_eratosfen(idx)", setup="from __main__ import find_simple_with_eratosfen; idx=50",
                    number=100))
# 74.7940787
print(timeit.timeit("find_simple_with_eratosfen(idx)", setup="from __main__ import find_simple_with_eratosfen; idx=200",
                    number=100))
# 73.2547682


# тут я оптимизирую алгоритм, увеличиваю длину цепочки , только если не найдено нужное число
def find_simple_with_eratosfen_refactor(idx):
    # список заполняется значениями от 0 до n
    max_n = 1000000
    n = 100
    simple_num_index = 1
    a = []
    for i in range(n + 1):
        a.append(i)
    simple_set = set()

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    while True:
        # начинаем с 3-го элемента
        i = 2
        while i <= n:
            # Если значение ячейки до этого не было обнулено,
            # в этой ячейке содержится простое число.
            if a[i] != 0:
                # если число искомое , возвращаем его
                if idx == simple_num_index:
                    return a[i]
                else:
                    if a[i] not in simple_set:
                        simple_num_index += 1
                        simple_set.add(a[i])
                        # первое кратное ему будет в два раза больше
                j = i + i
                while j <= n:
                    # это число составное, поэтому заменяем его нулем
                    a[j] = 0
                    # переходим к следующему числу, которое кратно i (оно на i больше)
                    j = j + i
            i += 1
        for i in range(n + 1, n + 101):
            a.append(i)
        n += 100
        if n > max_n:
            break
    # если в заданных границах так и не нашли число, возвращаем 0
    return 0


print(find_simple_with_eratosfen_refactor(idx))
#лучший результат получился
print(timeit.timeit("find_simple_with_eratosfen_refactor(idx)",
                    setup="from __main__ import find_simple_with_eratosfen_refactor; idx=50",
                    number=100))

#0.01906590000001529


print(timeit.timeit("find_simple_with_eratosfen_refactor(idx)",
                    setup="from __main__ import find_simple_with_eratosfen_refactor; idx=200",
                    number=100))

#0.3769484000000034