# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Вывести строку, содержащую эти же слова, разделенные одним
# символом «.» (точка). В конце строки точку не ставить
s = str(input("Введите любую фразу: "))

i = 0
while s[i] == ' ':
    i += 1
s = s[i:]

i = len(s)
while s[i - 1] == ' ':
    i -= 1
s = s[:i]

s_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        s_new += s[i]
    elif s[i - 1] != ' ':
        s_new += '.'
    i += 1
print(s_new + ' ')
