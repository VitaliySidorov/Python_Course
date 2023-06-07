# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) >0: return getNumber
        else: print(f"{getNumber} - Введите натуральное число.")

print('Программа заполнения массива элементами арифметической прогрессии.')
print('Введите первый элемент арифметической прогрессии: ')
a = int(getNumber_())
print('Введите шаг (разность) арифметической прогрессии: ')
d = int(getNumber_())
print('Введите количество элементов арифметической прогрессии: ')
n = int(getNumber_())

arProg = []
for i in range(n):
   arProg.append(a + i * d)

print(arProg)