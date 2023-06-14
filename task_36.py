# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) >0: return getNumber
        else: print(f"{getNumber} - Введите натуральное число.")


def print_operation_table(op, m, n):
    for i in range(1, m + 1):
        outRow = []                                 # создаем список строки
        for j in range(1, n + 1):
            outRow.append(str(op(i, j)))            # заполняем список строки элементами
        print(''.join(f'{e:<4}' for e in outRow))   # выравниваем вывод чисел в колонке и выводим на экран


print("Ведите количество строк: ")
num_rows = int(getNumber_())
print("Ведите количество столбцов: ")
num_columns = int(getNumber_())
print_operation_table(lambda num_rows, num_columns: num_rows*num_columns, num_rows, num_columns)
