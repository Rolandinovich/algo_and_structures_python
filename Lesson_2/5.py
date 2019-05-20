"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

char_table = {}
# как и договаривались на уроке создаю словарь кодов и символов
for i in range(32, 127):
    char_table[i] = chr(i)


def table_print(char_table, chr_num=32, n=10):
    if not char_table:
        return print('\n Готово')
    char = char_table.pop(chr_num)
    print(f'{str(chr_num).center(3)}={char}'.center(7), end='')
    if n == 1:
        print('')
        n = 11
    return table_print(char_table, chr_num + 1, n - 1)


table_print(char_table, 32, 10)
