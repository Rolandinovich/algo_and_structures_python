# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 9 + 1):
    count = 0
    for j in range(2, 99 + 1):
        if j % i == 0:
            count += 1
    print(f'{count} кратных чисел для {i}')
