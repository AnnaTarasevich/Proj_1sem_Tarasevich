# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия»
# добавить фразу «Министерства образования Ростовской области», посчитать количество произведённых добавлений.
# Сколько номеров телефонов заканчивается на «03», «50».
# Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re
p = re.compile(r'Горячая линия+')
s = re.compile(r'03+$', re.M)
k = re.compile(r'50+$', re.M)
m = re.compile(r'ЕГЭ.+\d+')

with open('hotline.txt', 'r+', encoding='utf-8') as f:
    text = f.read()
    z = re.sub('Горячая линия', 'Горячая линия Министерства образования Ростовской области', text)
    list1 = p.findall(text)
    list2 = s.findall(text)
    list3 = k.findall(text)

with open('hotline2.txt', 'w', encoding='utf-8') as f:
    f.write(z)

print('Количество произведенных добавлений: ', len(list1))
print('Количество номеров, заканчивающихся на 03: ', len(list2))
print('Количество номеров, заканчивающихся на 50: ', len(list3))
print('Номера телефонов горячих линий: ', m.findall(text))
print('Номера телефонов горячих линий: ', m.findall(text))