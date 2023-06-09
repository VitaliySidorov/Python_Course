# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import os, math

def clear_console(): # очистка консоли
  os.system('cls')

clear_console()

def getNumber_ (): # проверка правильности ввода
    while True:
        getNumber = input()  # Ввод числа
        if getNumber.isdigit() and int(getNumber) !=0 <= 1000: return getNumber
        else: print(f"{getNumber} - не натуральное число. Натуральные числа - числа, возникающие естественным образом при счете (1, 2, 3 и так далее...).")

print('Программа нахождения загаданных чисел m и n, если известно их произведение - q и сумма - p. Числа не больше 1000.')
print("Введите сумму чисел p: ")
p = int(getNumber_())
print("Введите произведение чисел q: ")
q = int(getNumber_())

# Решать задачу будем с помощью теоремы Виета. 
# Если q>0, то решения одинаковы по знаку и зависят от p, если p>0, то корни отрицательные.

d = p**2-4*q # находим дискиминант

if d <= 0:
    print("Решения нет. Числа не соответствуют условиям задачи.")
else:
    print(f"Первое число m = {int((-1*p + math.sqrt(d))/2)}")
    print(f"Второе число n = {int((-1*p - math.sqrt(d))/2)}")




