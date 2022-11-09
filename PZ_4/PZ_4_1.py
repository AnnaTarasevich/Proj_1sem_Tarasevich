#Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение
#выражения X - X^2/2 + X^3/3 - ... + (-1)^N-1X^N/N. Полученное число
#является приближенным значением функции ln в точке 1 +
import math
try:
  X = float(input("Введите X: "))
  N = int(input("Введите N: "))
except Exception:
  print('Вы ввели не число, введите снова: ')
  X = float(input("Введите X: "))
  N = int(input("Введите N: "))
p = 1
S = 0
i=N
while i<N+1:
    X **= p
    S += p/i
    p *= -1
    i = i+1
print("Result:")
print(S)
print("ln(x+1):")
print(math.log(X+1))