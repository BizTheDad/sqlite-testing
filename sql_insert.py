import sqlite3
from constants import NUM_DB
import random

with sqlite3.connect(NUM_DB) as connection:
    c = connection.cursor()

    c.execute("DROP TABLE if exists random_integers")

    c.execute("""
              CREATE TABLE random_integers
              (rand_num INT)
              """)

    for i in range(0, 100):
        c.execute("INSERT INTO random_integers VALUES(?)",
                  (random.randint(0, 100), ))
