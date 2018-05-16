import sqlite3
from constants import DB

with sqlite3.connect(DB) as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
