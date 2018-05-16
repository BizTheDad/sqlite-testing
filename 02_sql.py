import sqlite3
from constants import DB

conn = sqlite3.connect(DB)

cursor = conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

conn.commit()
conn.close()
