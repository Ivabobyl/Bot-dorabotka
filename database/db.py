
import sqlite3

def init_db():
    conn = sqlite3.connect("exchange.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        role TEXT DEFAULT 'user'
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        amount REAL,
        rate REAL,
        operator_id INTEGER,
        status TEXT DEFAULT 'pending'
    )""")
    conn.commit()
    conn.close()
