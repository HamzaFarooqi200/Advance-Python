import sqlite3

def manage_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    conn.commit()

    cursor.execute('SELECT * FROM users')
    print(cursor.fetchall())

    conn.close()

manage_database()


#********************** object manger ******************** 

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        self.value = value

singleton1 = Singleton('first')
singleton2 = Singleton('second')

print(singleton1.value)
print(singleton2.value) 
print(singleton1 is singleton2)


