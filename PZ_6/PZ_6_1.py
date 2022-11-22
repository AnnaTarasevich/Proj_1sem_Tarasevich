#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
#элементов списка, кроме элементов с номерами от K до L включительно.
import random
a = []
h = []
try:
    N = int(input("Введите количество элементов в списке: "))
    K = int(input("Введите L: "))
    L = int(input("Введите K: "))
except ValueError:
    print("Введите число заново")
    N = int(input("Введите количество элементов в списке: "))
    K = int(input("Введите L: "))
    L = int(input("Введите K: "))
for i in range(1, N):
    i += 2
    a.append(i)
    sum(a)
    for q in range(K+1, L-1):
        h.append(q)
        sum(h)
if K > 1 and K < L and L < N:
  p = sum(a)-sum(h)
  print(p)