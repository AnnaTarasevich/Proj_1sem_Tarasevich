# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел.
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

# Содержимое первого файла:
# Отрицательные элементы:
# Количество отрицательных элементов:
# Среднее арифметическое:

# Содержимое второго файла:
# Положительные элементы:
# Количество положительных элементов:
# Сумма положительных элементов:


import random
list1 = []
N = int(input("Введите количество элементов списка: "))
for i in range(N):
    list1.append(random.randint(-50, 50))
    list1.sort()
avr = 0
count = 0
list2 = []
for i in list1:
    if i < 0:
        list2.append(i)
        count += 1
for j in range(len(list2)):
    avr += list2[j]/count
avr1 = round(avr, 3)
f3 = open("data_3.txt", "w", encoding="utf-8")
f3.writelines("Содержимое первого файла: ")
f3.writelines(str(list1))
f3.write("\n")
f3.write("Отрицательные элементы: ")
f3.writelines(str(list2))
f3.write("\n")
f3.write("Количество отрицательных элементов: ")
f3.writelines(str(count))
f3.write("\n")
f3.write("Среднее арифметическое: ")
f3.writelines(str(avr1))
f3.close()

list3 = []
K = int(input("Введите количество элементов второго списка: "))
for i in range(K):
    list3.append(random.randint(-50, 50))
    list3.sort()
sum1 = 0
count = 0
list4 = []
for i in list3:
    if i > 0:
        list4.append(i)
        count += 1
for j in range(len(list4)):
    sum1 += list4[j]
f1 = open("data_4.txt", "w", encoding="utf-8")
f1.writelines("Содержимое второго файла: ")
f1.writelines(str(list3))
f1.write("\n")
f1.write("Положительные элементы: ")
f1.writelines(str(list4))
f1.write("\n")
f1.write("Количество положительных элементов: ")
f1.writelines(str(count))
f1.write("\n")
f1.write("Сумма положительных элементов: ")
f1.writelines(str(sum1))
f1.close()