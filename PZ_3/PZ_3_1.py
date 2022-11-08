# Проверить истинность высказывания:
#«Все цифры данного числа различны»
try:
    a = int(input('Введите число: '))
except Exception:
    print('Не то')
    a = int(input('Введите число: '))
else:
    b = int(a / 100)
    b1 = int((a - b * 100) / 10)
    b2 = a % 10
    if b != b1 and b1 != b2 and b != b2:
        print('Высказывание истинно')
    else:
        print('Высказывание ложно')