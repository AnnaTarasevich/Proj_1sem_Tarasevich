#В матрице найти минимальный элемент в предпоследней строке.

import random

i = int(input("Введите количество строк: "))
j = int(input("Введите количество столбцов: "))
m = [[random.randrange(1, 10) for y in range(j)] for x in range(i)]
for i in m:
    print(i)
k = len(m) - 2
print("Минимальный объект в предпоследней строке: ", min(m[k]))