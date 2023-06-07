# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    # while True:
    #     getNumber = input()  # Ввод числа
    #     if getNumber.isdecimal(): return getNumber
    #     else: print(f"{getNumber} - нецелое число.")
    while type:
        getNumber = input()                     # Ввод числа
        try:                                    # Проверка что getTempNumber преобразуется в число без ошибки
            getTempNumber = int(getNumber)
        except ValueError:                      # Проверка на ошибку неверного формата (введены буквы)
            print('"' + getNumber + '"' + ' - не является числом')
        else:                                   # Если getTempNumber преобразован в число без ошибки, выход из цикла while
            break
    return getNumber

print('Программа определения индексов чисел массива, принадлежащих заданному диапазону.')
print('Введите количество элементов множества n: ')
n = abs(int(getNumber_()))
print('Введите минимальную границу диапазона: ')
minN = int(getNumber_())
print('Введите максимальную границу диапазона: ')
maxN = int(getNumber_())

listN = [] # Создание массива чисел N

i = 0
while(i < n): # Заполняем массив случайными числами
    listN.append(random.randint(-99, 99))
    i += 1
print(listN)

count = 0
for j in range(len(listN)): # Проверка нахождения числа в указанном диапазоне
    if minN <= listN[j] <= maxN:
        print(f"Число {listN[j]} с индексом {j} находится в указанном диапазоне чисел [{minN};{maxN}].")
        count += 1

if count == 0: print(f"В заданном диапазоне [{minN};{maxN}] нет чисел из нашего множества.")