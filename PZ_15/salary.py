import sqlite3 as sq

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