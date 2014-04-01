import sqlite3

def create_table_join_table(cursor):
    cursor.execute('''CREATE TABLE animalsInZoo(name Text PRIMARY KEY ASC, zooId int, species Text, age int, gender Text, weight real, isAlive int)''')

conn = sqlite3.connect('animals.db')

cursor = conn.cursor()

create_table_join_table(cursor)

conn.commit()
conn.close()
