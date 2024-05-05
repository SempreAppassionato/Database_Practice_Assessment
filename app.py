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
while True:
    user_input = input("What would you like to do? \n 1. Print all airfract \n 2. Exit \n")
    if user_input == '1':
        print_all_aircraft()
    if user_input == '2':
        break
    else:
        print("Invalid input, please try again")