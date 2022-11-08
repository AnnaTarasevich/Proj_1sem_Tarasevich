# Даны два числа. Вывести порядковый номер меньшего из
# них
try:
  c = int(input('Введите число: '))
  b = int(input('Введите число: '))
except Exception:
  print("Не то")
  c = int(input('Введите число: '))
  b = int(input('Введите число: '))
else:
  print("Отлично)")
if c < b:
    print('1')
else:
    print('2')