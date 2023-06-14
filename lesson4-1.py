# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]

# outList = []

# for i in data:
#     if i%2 == 0:
#         outList.append((i, i**2))

# print(outList)

# ------------------------------------

# def select(f, col): # используем - map
#     return [f(x) for x in col]

# def where(f, col): # используем функцию - filter
#     return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
res = filter(lambda x: x%2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)