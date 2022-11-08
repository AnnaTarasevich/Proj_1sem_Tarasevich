# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE
try:
  N = int(input("Введите N: "))
except Exception:
  print("Введите целое число: ")
  N = int(input("Введите N: "))
  i = 1
  while True:
    if 3**i<N:
      i+=1
    else:
      print(3**i == N)
      break
else:
  i = 1
  while True:
    if 3**i<N:
      i+=1
    else:
      print(3**i == N)
      break