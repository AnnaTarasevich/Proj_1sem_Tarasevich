#Даны две последовательности. Найти элементы, различные для двух
#последовательностей и их среднее арифметическое.


from statistics import mean
list1 = [1, 2, 3, 4, 7, 8]
list2 = [1, 4, 5, 6]
list3 = [n for n in list1 if n not in list2] + [n for n in list2 if n not in list1]
print("Список различных для последовательностей чисел:", list3)
print("Среднее арифметическое чисел:", round(mean(list3), 2))