# Дан целочисленный список размера N. Если он является перестановкой, то есть
# содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
# первого недопустимого элемента.
try:
    N = int(input ("Введите количество элементов массива: "))
except ValueError:
    print("Введите число заново")
    N = int(input ("Введите количество элементов массива: "))
a = [int(i) for i in range(1, N + 1)]
for i in range(N):
    print("Введите элемент массива ", i + 1, ": ")
    tmp = int(input())
    if tmp in a :
        a.pop(a.index(tmp))
    else :
        print ('Первая ошибка появилась в символе номер ' + str(i + 1))
        break
if len(a) == 0 :
    print (str(0))