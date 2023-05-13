#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для определения дня недели, проверки на високосный год и определения
#количества дней в месяце.

import datetime


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_a_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            if self.leap_year():
                return 29
            else:
                return 28

    def day_of_week(self):
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        return days[datetime.date(self.year, self.month, self.day).weekday()]

#Тест
c = Calendar(2023, 5, 23)
print('Високосный год? ', c.leap_year())
print('Дней в месяце: ', c.days_in_a_month())
print('День недели: ',c.day_of_week())