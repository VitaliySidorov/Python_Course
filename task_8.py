# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить ровно k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

import os

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Не может быть {getNumber} долек в плитке шоколада.")

print('Программа для разделения плитки шоколада на части за один разлом.')
print('Введите ширину плитки шоколада - число n: ')
n = int(getNumber_())
print('Введите длину плитки шоколада - число m: ')
m = int(getNumber_())
print('Какое количество долек шоколада хотите - число k: ')
k = int(getNumber_())

if k < m*n and (k % m == 0 or k % n == 0):
    print('Разделить за один раз можно:')
    if k % m == 0:
        n1 = k // m
        print(f'- размер долек {n1}х{m}')
    if k % n == 0:
        m1 = k // n
        print(f'- размер долек {n}х{m1}')
else: print(f'Разделить плитку шоколада на {k} долек за один раз нельзя.')