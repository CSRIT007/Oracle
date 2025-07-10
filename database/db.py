import sqlite3
import os

DB_NAME = "school.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    # Only run if database doesn't exist
    if not os.path.exists(DB_NAME):
        conn = get_connection()
        with open('database/schema.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        cursor = conn.cursor()
        # Create a default admin user if not exists
        cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", "admin", "admin")
            )
            conn.commit()
        conn.close()
