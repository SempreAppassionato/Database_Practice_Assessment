#firstName-lastName MMXXIV

#imports the sqlite3 module
import sqlite3

#Constants and variables
DATABASE = 'fighters.db'

#functions
def print_all_aircraft():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    query = "SELECT * FROM fighter"
    cursor.execute(query)

    results = cursor.fetchall()
    #loop through the results and print them
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    db.close()

#main code
print_all_aircraft()