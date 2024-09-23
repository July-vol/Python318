
import sqlite3

toys_list = [
    ('Air', 1500),
    ('Ball', 500),
    ('Doll', 1000),
    ('Pion', 3500),
    ('Bear', 700),
    ('Dog', 5400),
    ('Pig', 2700),
    ('Caps', 2000),
    ('Flower', 900),
    ('Bird', 500),
]
with sqlite3.connect("toy.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS toys(
        toy_id INTEGER PRIMARY KEY AUTOINCREMENT,
        NameToy TEXT,
        Count TEXT
        price INTEGER
    )
    """)

for toy in toys_list:
    cur.executemany("INSERT INTO toys VALUES(NULL, ?, ?)", toys_list)

# #
# con.commit()
# con.close()
