#В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

import random

i = int(input("Введите количество строк и столбцов: "))
m1 = [[random.randrange(1, 10) for y in range(i)] for x in range(i)]
print("Получившаяся квадратная матрица:")
for i in m1:
    print(i)
m2 = [m1[i][i] for i in range(len(m1))]
m3 = [m1[i][i] * 2 for i in range(len(m1))]
print("Элементы главной диагонали: ", m2)
print("Элементы главной диагонали, увеличенные вдвое:", m3)
