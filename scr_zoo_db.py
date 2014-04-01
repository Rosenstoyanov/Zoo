import sqlite3

def create_table_users(cursor):#add
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY ASC, capacity int, budget real)''')


conn = sqlite3.connect("animals.db")

cT1 = conn.cursor()
create_table_users(cT1)

conn.commit()

conn.close()

#izvikvam tova vuv funkciq!!!!!!!!!
