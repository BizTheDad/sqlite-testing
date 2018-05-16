import sqlite3

conn = sqlite3.connect('C:/Users/Justin/PythonProjects/database/new.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE population(city TEXT, state TEXT, population INT)
               """)

conn.close()
