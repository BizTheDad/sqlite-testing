import sqlite3
from constants import DB

conn = sqlite3.connect(DB)

cursor = conn.cursor()

try:
    ny_insert = "INSERT INTO population VALUES('New York City', 'NY', 8400000)"
    sf_insert = "INSERT INTO population VALUES('San Francisco', 'CA', 800000)"
    cursor.execute(ny_insert)
    cursor.execute(sf_insert)
    conn.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

conn.close()
