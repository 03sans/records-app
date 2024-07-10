import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXIST users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)''')

conn.commit()

