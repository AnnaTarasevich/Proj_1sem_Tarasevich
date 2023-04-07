import sqlite3 as sq
from salary_data import *

with sq.connect('salary.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
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

#with sq.connect('salary.db') as con:
#    cur = con.cursor()
#    cur.executemany("INSERT INTO anketa VALUES (?,?,?,?,?,?,?,?,?)", info_anketa)

#with sq.connect('salary.db') as con:
#    cur = con.cursor()
#    cur.executemany("INSERT INTO sick_list VALUES (?,?,?,?,?,?,?)", info_list)

#1.Вывести список всех сотрудников и их должностей
#    cur.execute("""SELECT name, surname, post FROM anketa""")
#    result = cur.fetchall()
#print(result)

#2.Вывести список всех сотрудников и их базовых ставок
#    cur.execute("""SELECT name, surname, base_rate FROM anketa""")
#    result = cur.fetchall()
#print(result)

#3.Вывести список всех сотрудников, работающих в отделе "IT"
#    cur.execute(("""SELECT name, surname FROM anketa WHERE department = 'Отдел IT'"""))
#    result = cur.fetchall()
#print(result)

#4.Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
#    cur.execute("""SELECT name, surname FROM anketa WHERE hire_data > '2022-01-01'""")
#    result = cur.fetchall()
#print(result)

#5.Вывести список всех больничных листов, выписанных сотруднику с id = 42
#    cur.execute("""SELECT id_list, start_date, end_date FROM sick_list WHERE sick_list.id_sotr = 42""")
#    result = cur.fetchall()
#print(result)

#6.Вывести список всех больничных листов, оплаченных компанией
#    cur.execute("""SELECT id_list FROM sick_list WHERE paid = 1""")
#    result = cur.fetchall()
#print(result)

#7.Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
#    cur.execute("SELECT name, surname FROM anketa INNER JOIN "
#                "sick_list ON sick_list.id_sotr = anketa.id_sotr"
#               "WHERE end_date = '20")
#    result = cur.fetchall()
#print(result)

#8.Вывести среднюю базовую ставку всех сотрудников
#    cur.execute("""SELECT AVG(base_rate) FROM anketa""")
#    result = cur.fetchall()
#print(result)

#9.Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
#    cur.execute("SELECT id_sotr, name, surname FROM anketa WHERE base_rate > 100000")
#    result = cur.fetchall()
#print(result)

#10.Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
#    cur.execute("SELECT anketa.name, anketa.surname, "
#                "SUM(julianday(sick_list.end_date) - julianday(sick_list.start_date)) "
#                "FROM anketa INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                "GROUP BY anketa.name, anketa.surname")
#    result = cur.fetchall()
#print(result)

#11.Вывести информацию о сотрудниках и их больничных листах за последний месяц
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr WHERE "
#                "sick_list.start_date >= DATE('now', '-3 month')")
#    result = cur.fetchall()
#print(result)

#12.Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
#    cur.execute("SELECT department, AVG(julianday(end_date) - julianday(start_date) + 1) FROM anketa "
#                        "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr GROUP BY department")
#    result = cur.fetchall()
#print(result)

#13.Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                 "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                 "WHERE sick_list.start_date = (SELECT MIN(start_date) "
#                 "FROM sick_list WHERE sick_list.id_sotr = anketa.id_sotr)")
#    result = cur.fetchall()
#print(result)

#14. Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
#    cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                "WHERE sick_list.start_date = (SELECT MIN(start_date) "
#                "FROM sick_list WHERE sick_list.id_sotr = anketa.id_sotr)")
#    result = cur.fetchall()
#print(result)

#15.Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
#    cur.execute("SELECT name, surname, SUM(julianday(end_date) - julianday(start_date)) AS summa  FROM anketa "
#                "INNER JOIN sick_list ON anketa.id_sotr = sick_list.id_sotr "
#                "WHERE strftime('%Y', start_date) = strftime('%Y', 'now') "
#                "GROUP BY name, surname ORDER BY summa")
#    result = cur.fetchall()
#print(result)