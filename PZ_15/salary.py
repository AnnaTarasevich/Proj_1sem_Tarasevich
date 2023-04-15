import sqlite3 as sq
from salary_data import *

with sq.connect('salary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
     id_sotr INTEGER PRIMARY KEY,
     name VARCHAR,
     surname VARCHAR,
     birth_date DATE,
     sex VARCHAR,
     hire_data DATE,
     post VARCHAR,
     department VARCHAR,
     base_rate DECIMAL
     )""")

with sq.connect('salary.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sick_list (
    id_list INTEGER PRIMARY KEY,
    id_sotr INTEGER,
    start_date DATE,
    end_date DATE,
    reason VARCHAR,
    diagnosis VARCHAR,
    paid BOOLEAN,
    FOREIGN KEY(id_sotr) REFERENCES salary(id_sotr) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

# with sq.connect('salary.db') as con:
#    cur = con.cursor()
#    cur.executemany("INSERT INTO anketa VALUES (?,?,?,?,?,?,?,?,?,?)", info_anketa)

with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.executemany("INSERT INTO sick_list VALUES (?,?,?,?,?,?,?)", info_list)


# Добавила колонку raising, в которой указано, получил ли сотрудник повышение
# with sq.connect('salary.db') as con:
#    cur = con.cursor()
#    cur.execute("""ALTER TABLE anketa ADD raising boolean""")


"""SELECT"""
# 1.Вывести список всех сотрудников и их должностей
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("""SELECT name, surname, post FROM anketa""")
#    result = cur.fetchall()
#print(result)

# 2.Вывести список всех сотрудников и их базовых ставок
#    cur.execute("""SELECT name, surname, base_rate FROM anketa""")
#    result = cur.fetchall()
#print(result)

# 3.Вывести список всех сотрудников, работающих в отделе "IT"
#    cur.execute(("""SELECT name, surname FROM anketa WHERE department = 'Отдел IT'"""))
#    result = cur.fetchall()
#print(result)

# 4.Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
#    cur.execute("""SELECT name, surname FROM anketa WHERE hire_data > '2022-01-01'""")
#    result = cur.fetchall()
#print(result)

# 5.Вывести список всех больничных листов, выписанных сотруднику с id = 42
#    cur.execute("""SELECT id_list, start_date, end_date FROM sick_list WHERE sick_list.id_sotr = 42""")
#    result = cur.fetchall()
#print(result)

# 6.Вывести список всех больничных листов, оплаченных компанией
#    cur.execute("""SELECT id_list FROM sick_list WHERE paid = 1""")
#    result = cur.fetchall()
#print(result)

# 7.Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
#    cur.execute("SELECT anketa.name, anketa.surname FROM anketa INNER JOIN sick_list ON "
#                "anketa.id_sotr = sick_list.id_sotr WHERE strftime('%m', sick_list.start_date) = strftime('%m', 'now')")
#    result = cur.fetchall()
#print(result)

# 8.Вывести среднюю базовую ставку всех сотрудников
#    cur.execute("""SELECT AVG(base_rate) FROM anketa""")
#    result = cur.fetchall()
# print(result)

# 9.Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
#    cur.execute("SELECT id_sotr, name, surname FROM anketa WHERE base_rate > 100000")
#    result = cur.fetchall()
# print(result)

# 10.Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
#    cur.execute("SELECT anketa.name, anketa.surname, "
#                "SUM(julianday(sick_list.end_date) - julianday(sick_list.start_date)) "
#                "FROM anketa INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                "GROUP BY anketa.name, anketa.surname")
#    result = cur.fetchall()
# print(result)

# 11.Вывести информацию о сотрудниках и их больничных листах за последний месяц
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr WHERE "
#                "sick_list.start_date >= DATE('now', '-1 month')")
#    result = cur.fetchall()
#print(result)

# 12.Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
#    cur.execute("SELECT department, AVG(julianday(end_date) - julianday(start_date) + 1) FROM anketa "
#                        "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr GROUP BY department")
#    result = cur.fetchall()
# print(result)

with sq.connect('salary.db') as con:
    cur = con.cursor()
# 13.Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                 "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                 "WHERE sick_list.start_date = (SELECT MAX(start_date) "
#                 "FROM sick_list WHERE sick_list.id_sotr = anketa.id_sotr)")
#    result = cur.fetchall()
# print(result)

# 14. Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                "WHERE sick_list.start_date = (SELECT MIN(start_date) "
#                "FROM sick_list WHERE sick_list.id_sotr = anketa.id_sotr)")
#    result = cur.fetchall()
# print(result)

# 15.Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
    cur.execute("SELECT name, surname, SUM(julianday(end_date) - julianday(start_date)) AS summa FROM anketa "
                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
                "WHERE strftime('%Y', start_date) = strftime('%Y', 'now') "
                "GROUP BY name, surname ORDER BY summa")
    result = cur.fetchall()
print(result)

"""UPDATE"""
with sq.connect('salary.db') as con:
    cur = con.cursor()
# 1.Обновить базовую ставку сотрудника на определенной должности
#    cur.execute("""UPDATE anketa SET base_rate = 40000 WHERE post = 'Медбрат'""")

# 2.Обновить отдел для всех сотрудников в определенном диапазоне возраста.
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("""UPDATE anketa SET department = 'Администрация' WHERE birth_date BETWEEN '2000-01-31' AND '2015-08-31'""")

# 3.Обновить дату найма для сотрудника, получившего повышение.
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("""UPDATE anketa SET hire_data = '2023-04-08' WHERE raising = '1'""")

# 4.Обновить причину больничного листа для сотрудника
with sq.connect('salary.db') as con:
    cur = con.cursor()
#   cur.execute("""UPDATE sick_list SET reason = 'Отравление' WHERE id_list = 8""")

# 7.Обновить причину больничного листа в таблице "Больничные листы" на
# определенное значение для всех сотрудников, работающих в отделе "Бухгалтерия".
with sq.connect('salary.db') as con:
    cur = con.cursor()
#     cur.execute("UPDATE sick_list SET reason = 'Перелом' WHERE id_sotr "
#                 "IN (SELECT id_sotr FROM anketa WHERE department = 'Бухгалтерия')")


"""DELETE"""
# 1.Удалить все записи о больничных листах для сотрудника с именем "Иван"!!!!!!!
with sq.connect('salary.db') as con:
    cur = con.cursor()
#   cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE name = 'Иван')")

# 2.Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE surname = 'Петров')")

# 3.Удалить все записи о больничных листах для сотрудника с должностью "Менеджер"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE post = 'Менеджер')")

# 4.Удалить все записи о больничных листах для сотрудника с отделом "Отдел продаж"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE department = 'Отдел продаж')")

# 5.Удалить все записи о больничных листах для сотрудника женского пола
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE sex = 'ж')")

# 6.Удалить все записи о больничных листах для сотрудников старше 50 лет
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id_sotr FROM anketa WHERE birth_date < '1973-01-01')")

# 7.Удалить все записи о неоплаченных больничных листах
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE paid = 0")

# 8.Удалить все записи о больничных листах, дата окончания которых прошла
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE end_date < DATE('now')")

# 9.Удалить все записи о больничных листах, начиная с определенной даты
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE start_date >= DATE('2022-01-05')")

# 10.Удалить все записи о больничных листах, закончившихся до определенной даты
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE end_date <= DATE('2020-01-01')")

# 11.Удалить все больничные листы сотрудника с именем "Иван" из таблицы "Больничные листы"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id_sotr FROM anketa WHERE name = 'Иван')")

# 12.Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву "С" из таблицы "Больничные листы"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id_sotr FROM anketa WHERE surname LIKE 'С%')")

# 13.Удалить все больничные листы, которые еще не были оплачены, у сотрудников с должностью "Менеджер" из таблицы "Больничные листы"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute(" DELETE FROM sick_list WHERE paid = 0 AND id_sotr "
#                "IN (SELECT id_sotr FROM anketa WHERE post = 'Менеджер')")

# 14.Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1 января
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id_sotr FROM anketa WHERE department = 'Отдел IT') "
#                "AND start_date >= '2022-01-01'")

# 15.Удалить все больничные листы, связанные со сотрудниками старше 50 лет из таблицы "Больничные листы"
with sq.connect('salary.db') as con:
    cur = con.cursor()
#    cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id_sotr FROM anketa WHERE birth_date<= '1973-01-01')")

#with sq.connect('salary.db') as con:
#    cur = con.cursor()
#    cur.execute("INSERT INTO sick_list values (18, 9, '2023-04-23', '2023-04-25', 'Болезнь', 'Ангина', 1)")