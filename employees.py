import csv
import sqlite3
from constants import DB, EMP_CSV

with sqlite3.connect(DB) as conn:
    c = conn.cursor()

    employees = csv.reader(open(EMP_CSV, 'rU'))

    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)",
                  employees)
