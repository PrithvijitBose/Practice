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
    note_id= cur.lastrowid
    conn.commit()
    conn.close()
    return note_id

def get_note_by_id(note_id):
    conn= sqlite3.connect("notes.db")
    cur = conn.cursor()
    res=cur.execute("""SELECT * FROM notes  WHERE id=?""",(note_id,))
    note = res.fetchone()
    conn.close()
    return note

def get_note_all():
    conn=sqlite3.connect('notes.db')
    cur=conn.cursor()
    res=cur.execute('''SELECT * from notes''')
    notes=res.fetchall()
    conn.close()
    return notes

def update_note(title,category,content,note_id):
    conn=sqlite3.connect('notes.db')
    cur=conn.cursor()
    res=cur.execute("""UPDATE notes
                    SET title=?,
                    category=?,
                    content=?
                    WHERE id = ?
                    
    """,(title,category,content,note_id))
    updated_rows=cur.rowcount
    conn.commit()
    conn.close()
    return updated_rows

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cur=conn.cursor()
    res=cur.execute("""DELETE from notes WHERE id=?""",(note_id,))
    deleted_rows = cur.rowcount
    conn.commit()
    conn.close()
    return deleted_rows