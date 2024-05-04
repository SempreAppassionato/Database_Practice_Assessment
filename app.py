import sqlite3

db = sqlite3.connect('fighters.db')
cursor = db.cursor()

query = "SELECT * FROM fighter"
cursor.execute(query)

results = cursor.fetchall()
print(results)
db.close()