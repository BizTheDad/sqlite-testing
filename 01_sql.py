import sqlite3
from constants import DB

conn = sqlite3.connect(DB)

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE population(city TEXT, state TEXT, population INT)
               """)

conn.close()
