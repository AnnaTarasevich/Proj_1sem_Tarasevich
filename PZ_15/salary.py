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
#    cur.execute()
#    result = cur.fetchall()
#print(result)

#11.Вывести информацию о сотрудниках и их больничных листах за последний месяц
#    cur.execute()
#        result = cur.fetchall()
#print(result)

#12.Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
#    cur.execute()
#        result = cur.fetchall()
#print(result)

#13.Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
    cur.execute("SELECT * FROM sick_list INNER JOIN "
                "anketa ON sick_list.id_sotr = anketa.id_sotr")
    result = cur.fetchall()
print(result)