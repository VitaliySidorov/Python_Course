# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) >= 0: return getNumber
        else: print(f"{getNumber} - Введите целое неотрицательное число.")

def summ(a, b):
   if(b == 0):
      return(a)
   return(summ(a + 1, b - 1))

print('Программа нахождения суммы целых неотрицательных чисел A и B с помощью рекурсии.')
print('Введите число А: ')
a = int(getNumber_())
print('Введите число B: ')
b = int(getNumber_())

print(f"Сумма чисел {a} и {b} равна ", summ(a, b))