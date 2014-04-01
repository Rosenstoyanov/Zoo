import sqlite3

def create_table_users(cursor):#add
    cursor.execute('''CREATE TABLE ClassZoo(id INTEGER PRIMARY KEY ASC, capacity REAL, email REAL''')


conn = sqlite3.connect("animals.db")

cT1 = conn.cursor()
create_table_users(cT1)

conn.commit()

conn.close()

#izvikvam tova vuv funkciq!!!!!!!!!
