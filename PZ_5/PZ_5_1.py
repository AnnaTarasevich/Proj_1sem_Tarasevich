# Составить функцию, которая выполнит суммирования числового ряда.
try:
  x = int(input("Введите последнее число: "))
  x = int(x)
except ValueError:
  print("Вы ввели не тот тип данных, введите заново: ")
  x = int(input("Введите последнее число: "))
def sum_numbers(x):
    z = 1
    s = 0
    while z <= x:
        s = z + s
        z += 1
 # for i in range(1,x+1):
    return s
print("Сумма ряда: ", sum_numbers(x))
