# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

data = '1 2 3 5 8 15 23 38'
print(data)

data = list(map(int, data.split()))
print(data)