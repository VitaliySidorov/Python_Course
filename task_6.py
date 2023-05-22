# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

import os

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input('Введите номер билета: ')  # Ввод числа
        if getNumber.isdigit() and int(getNumber) < 1000000 and len(getNumber) == 6: return getNumber
        else: print(f"{getNumber} - неверный ввод числа. Введите шестизначный номер на билете.")

def sumNumbers_(num: int):
    sum = 0
    while num > 0: # разбиение числа на цифры по разрядам
        x = num % 10
        sum = sum + x
        num = num // 10
    return sum

print('Программа определения счастливого номера на билете.')
n = int(getNumber_())

Number = n // 1000 # выделяем левую часть номера
Left = sumNumbers_(Number)

Number = n % 1000 # выделяем правую часть номера
Right = sumNumbers_(Number)

if Left == Right: print('Билет счастливый!')
else: print('Билет несчастливый.')
