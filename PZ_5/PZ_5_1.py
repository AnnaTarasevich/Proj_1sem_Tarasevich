# Составить функцию, которая выполнит суммирования числового ряда
try:
  # y = int(input("введите первое чсло ряда: "))
  x = int(input("Введите последнее число: "))
  x = int(x)
except ValueError:
  print("Вы ввели не тот тип данных, введите заново: ")
  # y = int(input("введите первое чсло ряда: "))
  x = int(input("Введите последнее число: "))
s=0
def sum_numbers(s):
 for i in range(1,x+1):
    s=i+s
 return s
print("Сумма ряда: ", sum_numbers(s))