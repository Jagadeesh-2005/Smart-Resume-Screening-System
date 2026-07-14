import sqlite3

conn = sqlite3.connect("database/candidates.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score REAL,
    recommendation TEXT
)
""")

conn.commit()
conn.close()