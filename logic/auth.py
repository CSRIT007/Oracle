import sqlite3

def verify_login(username, password):
    # Connect to your SQLite database file. Adjust path if needed!
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    # Query uses password_hash
    cur.execute(
        "SELECT user_id, role FROM users WHERE username=? AND password_hash=?",
        (username, password)
    )
    row = cur.fetchone()
    conn.close()
    if row:
        # Return just the role (old style), or dict (new style, see below for full login info)
        return row[1]
    return None

# (Optional) Helper: get user dict for session
def get_user_by_username(username):
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("SELECT user_id, username, role, created_at, last_login FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {
            "user_id": row[0],
            "username": row[1],
            "role": row[2],
            "created_at": row[3],
            "last_login": row[4]
        }
    return None

# (Optional) Hash password for better security (for demo: plain)
# import hashlib
# def hash_password(pw):
#     return hashlib.sha256(pw.encode()).hexdigest()
