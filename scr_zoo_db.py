import sqlite3

def create_table_users(cursor):#add
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY ASC, name Text, email Text)''')


conn = sqlite3.connect("dataBase.db")

cT1 = conn.cursor()
create_table_users(cT1)

conn.commit()

conn.close()

#izvikvam tova vuv funkciq!!!!!!!!!
