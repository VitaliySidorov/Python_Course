# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

def expon(base, exp):
   if(exp == 1):
      return(base)
   if(exp != 1):
      return(base * expon(base, exp - 1))

print('Программа возведения числа A в степень B с помощью рекурсии.')
print('Введите основание степени А: ')
a = int(getNumber_())
print('Введите показатель степени B: ')
b = int(getNumber_())

print(f"Результат возведения числа {a} в степень {b} -> ", expon(a, b))