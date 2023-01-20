# Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.

t = 0
list2 = ['.', ',', '!', '?']
for i in open('text18-21.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        for p in list2:
            if j == p:
                t += 1
print('\n')
print('Количество знаков препинания: ', t, end='\n')
f1 = open('text18-21.txt', encoding='UTF-8')
list1 = f1.readlines()
list1.reverse()
list1.insert(1, '\n')
f2 = open('text18-21_1.txt', 'w',  encoding='UTF-8')
f2.writelines(list1)
f2.close()