import sqlite3
import re
import os

SCHEMA_FILE = os.path.join('database', 'schema.sql')
DB_FILE     = 'school.db'

def run_schema():
    # 1) connect and enforce foreign keys
    conn = sqlite3.connect(DB_FILE)
    conn.execute('PRAGMA foreign_keys = ON')
    cur = conn.cursor()

    # 2) read your schema file
    with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
        raw_sql = f.read()

    # 3) split into statements (on semicolons)
    statements = [stmt.strip()
                  for stmt in re.split(r';\s*(?=\n|$)', raw_sql)
                  if stmt.strip()]

    for stmt in statements:
        # 4) if it's an INSERT, make it IGNORE duplicates
        if stmt.upper().startswith('INSERT INTO'):
            stmt = re.sub(r'INSERT\s+INTO',
                          'INSERT OR IGNORE INTO',
                          stmt, count=1, flags=re.IGNORECASE)

        try:
            cur.execute(stmt)
        except sqlite3.OperationalError as e:
            errmsg = str(e).lower()
            if 'already exists' in errmsg:
                print(f"↩︎ skipping existing object: {stmt.splitlines()[0][:50]} …")
                continue
            else:
                raise
        except sqlite3.IntegrityError as e:
            errmsg = str(e).lower()
            if 'unique constraint failed' in errmsg:
                print(f"↩︎ skipping duplicate row: {stmt.splitlines()[0][:50]} …")
                continue
            else:
                raise

    conn.commit()
    conn.close()
    print("✔️  Schema applied (new objects created, duplicates ignored).")


if __name__ == '__main__':
    run_schema()
