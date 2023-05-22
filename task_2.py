# Задача 2: Найдите сумму цифр трехзначного числа.

import os

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input('Введите любое натуральное число: ')  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

print('Программа нахождения суммы цифр в числе.')
n = int(getNumber_())
number = n
summa = 0

while n > 0: # разбиение числа на цифры по разрядам
    x = n % 10
    summa = summa + x
    n = n // 10
    
print(f'Сумма цифр числа {number} = {summa}')
