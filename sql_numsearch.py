import sqlite3
from constants import NUM_DB

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

with sqlite3.connect(NUM_DB) as connection:
    c = connection.cursor()

    funcs = {1: "avg", 2: "max", 3: "min", 4: "sum"}

    while True:
        sql_func = input(prompt)

        if int(sql_func) == 5:
            print("Exiting")
            break
        elif int(sql_func) in funcs:
            c.execute("""
                      SELECT {}(rand_num) FROM random_integers
                      """.format(funcs[int(sql_func)]))

            print("Result: " + str(c.fetchone()[0]))
