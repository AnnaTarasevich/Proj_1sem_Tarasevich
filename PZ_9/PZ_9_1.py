# Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
# информацию из строки в словарь, найти среднее арифметическое оценок,
# результаты вывести на экран.
str1 = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
student = {}
a = str1.split()
student["Фамилия"] = a[0]
student['Имя'] = a[1]
student['Группа'] = a[2]
student['Оценки'] = a[3:]
n = 0
for i in a[3::]:
  n += int(i)
student['Среднее арифметическое'] = n / len(a[3::])
for n in student.items():
  print(n)