# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

import os

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input('Введите любое натуральное число n: ')  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

print('Программа нахождения степени числа 2, не превышающих числа n.')
n = int(getNumber_())
list_2 = []
i = 0

while 2**i <= n:
    list_2.append(i)
    i += 1

print(f"Степени числа 2, не превышающие {n}:", list_2)