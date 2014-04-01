import sqlite3

def create_table_join_table(cursor):
    cursor.execute('''CREATE TABLE animalsInZoo(animalNumber INTEGER PRIMARY KEY ASC, zooId int, species int, name Text, age int, gender Text, weight real, isAlive int)''')

conn = sqlite3.connect('animals.db')

cursor = conn.cursor()

create_table_join_table(cursor)

conn.commit()
conn.close()
