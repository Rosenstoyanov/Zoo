import sqlite3

def create_table_join_table(cursor):
    cursor.execute('''CREATE TABLE animalsInZoo(id INTEGER PRIMARY KEY ASC, zooId int, animalId int, name Text, age int, gender Text, weight real)''')

conn = sqlite3.connect('animals.db')

cursor = conn.cursor()

create_table_join_table(cursor)

conn.commit()
conn.close()
