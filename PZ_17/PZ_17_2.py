#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
#"кличка" и "порода".

class Animal:
    def __init__(self, species, legs, color):
        self.species = species
        self.legs = legs
        self.color = color

class Dog(Animal):
    def __init__(self, species, legs, color, name, breed):
        Animal.__init__(self, species, legs, color)
        self.name = name
        self.breed = breed




#Тест
d = Dog('Собака', 4, 'Коричневый', 'Шарик', 'Лабрадор')
print('Вид: ', d.species)
print('Количество лап: ', d.legs)
print('Цвет: ', d.color)
print('Кличка: ', d.name)
print('Порода: ', d.breed)

c = Animal('Птица', 2, 'Розовый')
print('Вид: ', c.species)
print('Количество лап: ', c.legs)
print('Цвет: ', c.color)