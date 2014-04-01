class ZooInterface():
    """docstring for ZooInterface"""
    def __init__(self):
        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

    def close_connection():
        self.conn.close()

    def list_employees():#ne e taka
        open_connection()
        sql_query = "SELECT * FROM companies"
        result = cursor.execute(sql_query)
        for row in result:
            print(row)
        close_connection()

    def see_animals():
        sql_query = "SELECT name, species, age, weight FROM animals"

    def add(self, name, mail):
        sql_query = "INSERT INTO users(name) VALUES(?,)"
        sql_query2 = "INSERT INTO mail(mail) VALUES(?,)"
        cursor.execute(sql_query, (name, ))
        cursor.execute(sql_query2, (mail, ))
        close_connection()

