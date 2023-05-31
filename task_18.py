# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import os, random

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

def findClosest(uniqueNumbers, size, m): # процедура поиска ближайшего числа методом бинарного поиска
    # Проверка крайних чисел
    if (m <= uniqueNumbers[0]):
        return uniqueNumbers[0]
    if (m >= uniqueNumbers[size - 1]):
        return uniqueNumbers[size - 1]
 
    # Алгоритм бинарного поиска
    i = 0
    j = size
    mid = 0
    while (i < j):
        mid = (i + j) // 2
        if (uniqueNumbers[mid] == m):
            return uniqueNumbers[mid]
 
        # Если число меньше чем средний элемент массива, то ищем слева
        if (m < uniqueNumbers[mid]):
 
            # Если число больше предыдущего, но меньше среднего, то возвращаем ближайший из двух
            if (mid > 0 and m > uniqueNumbers[mid - 1]):
                return getClosest(uniqueNumbers[mid - 1], uniqueNumbers[mid], m)
 
            # Повторяем для левой части
            j = mid
 
        else: # Иначе, если число больше среднего, но меньше последующего, то возвращаем ближайший из двух
            if (mid < size - 1 and m < uniqueNumbers[mid + 1]):
                return getClosest(uniqueNumbers[mid], uniqueNumbers[mid + 1], m)
 
            i = mid + 1
 
    # После поиска остается только один элемент
    return uniqueNumbers[mid]
 
 
# Метод сравнения значений, какое из них наиболее близко.
# Находим наиболее близкое значение, взяв разницу между m и обоими значениями. 
# При этом предполагается, что val2 больше, чем val1, а n лежит между ними.
def getClosest(val1, val2, m):
    if (m - val1 >= val2 - m):
        return val2
    else:
        return val1

print('Программа нахождения самого близкого числа к искомому в массиве случайных чисел.')
print('Введите количество элементов в массиве: ')
n = int(getNumber_())
print('Введите искомое число: ')
m = int(getNumber_())

listNumber = [] # Создание списка чисел
uniqueNumbers = []
i = 0
while(i <= n and n > len(uniqueNumbers)):
    listNumber.append(random.randint(0, n**2))
    uniqueNumbers = list(set(listNumber))
    i += 1

uniqueNumbers.sort()
size = len(uniqueNumbers)
print(uniqueNumbers)

print(f"Наиболее близкое к числу {m} - число ", findClosest(uniqueNumbers, size, m))