#Из заданной строки отобразить только цифры. Использовать библиотекуstring.
#Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
#481 feet (147 metres) high

from string import digits

str1 = "he Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230 metres) " \
        "long and 481 feet (147 metres) high."
str2 = [i for i in str1 if i in digits]
print("Цифры из заданной строки:", ",".join(str2))