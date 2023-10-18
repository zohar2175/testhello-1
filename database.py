import sqlite3

conn = sqlite3.connect('messages.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_address TEXT,
    message TEXT
)
''')

conn.commit()
conn.close()
