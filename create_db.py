import sqlite3
conn = sqlite3.connect("database.db")

print("Database connected.")

cmd = "CREATE TABLE students (name TEXT, addr TEXT, city TEXT, zip TEXT)"

conn.execute(cmd)

print("Table created successfully.")

conn.close()