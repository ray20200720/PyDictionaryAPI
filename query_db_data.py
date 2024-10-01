import sqlite3

conn = sqlite3.connect("dictionary.db")

cursor = conn.cursor()

cursor.execute('SELECT * FROM words')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

