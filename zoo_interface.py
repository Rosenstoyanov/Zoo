class ZooInterface():
    """docstring for ZooInterface"""
    def __init__(self):
        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

    def close_connection():
        self.conn.close()

    def see_animals(self):
        sql_query = "SELECT name, species, age, weight FROM animals"
        result = self.cursor.execute(sql_query)
        for row in result:
            print(row)
        close_connection()

    def accommodate (self, species, name, age, weight):
        sql_query = "INSERT INTO animalsinZoo VALUES()"


