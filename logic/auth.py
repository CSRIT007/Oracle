from database.db import get_connection

def verify_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, role, password_hash FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and password == result[2]:
        return {"user_id": result[0], "role": result[1]}
    return None
