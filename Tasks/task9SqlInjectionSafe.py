import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

username = input("Username: ")
cur.execute("SELECT * FROM users WHERE username = ?", (username,))

user = cur.fetchone()
if user:
    print("User found:", user)
else:
    print("No user found")
