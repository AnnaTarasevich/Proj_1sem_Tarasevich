# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Вывести строку, содержащую эти же слова, разделенные одним
# символом «.» (точка). В конце строки точку не ставить.
try:
  s = str(input("Введите фразу: "))
except:
  print("Ошибка, введите другую фразу: ")
  s = str(input("Введите фразу: "))
f = str.replace(s," ",".")
print(f)