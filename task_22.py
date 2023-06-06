# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

print('Программа нахождения одинаковых чисел в двух множествах.')
print('Введите количество элементов множества n: ')
n = int(getNumber_())
print('Введите количество элементов множества m: ')
m = int(getNumber_())

setN = set() # Создание множества чисел N
setM = set() # Создание множества чисел M

i = 0
while(i <= n):
    setN.add(random.randint(0, 99))
    i += 1

j = 0
while(j <= m):
    setM.add(random.randint(0, 99))
    j += 1

print(setN)
print(setM)

SameNumbers = setN.intersection(setM)

if(len(SameNumbers)!=0):
    print(SameNumbers)
else:
    print("Совпадающих чисел в обоих множествах нет.")