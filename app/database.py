import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users(username,password,points)""")
conn.commit()
