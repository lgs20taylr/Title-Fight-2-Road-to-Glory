import sqlite3

class player():
    def __init__(self,id,firstName,lastName,age):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    
    def load():
        print("a")

connection = sqlite3.connect("rtgdatabase.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY,firstName TEXT,lastName TEXT,age INTEGER)")

cursor.execute("INSERT INTO players (firstName,lastName,age) VALUES ('Lionel','Messi',36)")

cursor.execute("SELECT * FROM players WHERE id = 1")

a = cursor.fetchall()
print(a)

connection.commit()

connection.close()