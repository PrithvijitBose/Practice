import sqlite3


def create_database():
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_note(title, content, category):
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO notes (title, content, category)
        VALUES (?, ?, ?)
    """, (title, content, category))
    print(f"Last inserted row ID: {cur.lastrowid}")
    conn.commit()
    conn.close()

def get_note_by_id(note_id):
    conn= sqlite3.connect("notes.db")
    cur = conn.cursor()
    res=cur.execute("""SELECT * FROM notes  WHERE id=?""",(note_id,))
    note = res.fetchone()
    conn.close()
    return note