# Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
# или отрицательного параметра A функция возвращает 0. С помощью этой функции
# найти степени AP, BP, CP, если даны числа P, A, B, C.
import math
try:
     a = float(input("Введите A: "))
     a = float(a)
except ValueError:
     print("Вы ввели не тот тип данных, введите любое число: ")
     a = float(input("Введите A: "))
try:
     b = float(input("Введите B: "))
     b = float(b)
except ValueError:
     print("Вы ввели не тот тип данных, введите любое число: ")
     b = float(input("Введите B: "))
try:
     p = int(input("Введите P: "))
     p = int(p)
except ValueError:
     print("Вы ввели не тот тип данных, введите любое число: ")
     p = int(input("Введите P: "))

try:
     c = float(input("Введите C: "))
     c = float(c)
except ValueError:
     print("Вы ввели не тот тип данных, введите любое число: ")
     c = float(input("Введите C: "))
else:
   def Power1(a,b):
     if a <= 0:
       print("0")
     else:
      result = math.exp(b*math.log(a))
      return result
   if a<=0:
     print("0")
   else:
     print("A^P: ", Power1(a,p))
     print("C^P: ", Power1(c,p))
     print("B^P: ", Power1(b,p))