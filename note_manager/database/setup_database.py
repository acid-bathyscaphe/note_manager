import sqlite3

def setup_database(db_path):#функция для создания базы данных если её нет
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT NOT NULL,
    created_date TEXT NOT NULL,
    issue_date TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def save_note_to_db(note, db_path):#функция для сохранения заметки в базу данных
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes (username, title, content, status, created_date, issue_date) VALUES (?, ?, ?, ?, ?, ?); """,
                   (note['username'], note['title'], note['content'], note['status'], note['created_date'], note['issue_date']))

    connection.commit()
    connection.close()

def load_notes_from_db(db_path):#функция для загрузки заметки из базы данных
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes;")
    rows = cursor.fetchall()
    notes = []

    for row in rows:
        notes.append({
            'id': row[0],
            'username': row[1],
            'title': row[2],
            'content': row[3],
            'status': row[4],
            'created_date': row[5],
            'issue_date': row[6],
        })
    connection.close()
    return notes

def update_note_in_db(note_id, updates, db_path):#функция для обновления указаной заметки в базе данных
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE notes
        SET username = ?, title = ?, content = ?, status = ?, issue_date = ?
        WHERE id = ?;
        """,(updates['username'],updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))

    connection.commit()
    connection.close()

def delete_note_from_db(note_id, db_path):#функция для удаления заметки из базы данных по id
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM notes WHERE id = ?;", (note_id,))

    connection.commit()
    connection.close()

def search_notes_by_keyword(keyword, db_path):#функция которая находит заметки в базе данных по ключевому слову и возвращает список словарей
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ?;
    """, (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()
    connection.close()
    return [{'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4], 'created_date': row[5], 'issue_date': row[6]} for row in rows]

def filter_notes_by_status(status, db_path):#функция которая находит заметки в базе данных по статусу и возвращает список словарей
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM notes WHERE status LIKE (?);""", (status,))

    rows = cursor.fetchall()
    connection.close()
    return [{'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4], 'created_date': row[5], 'issue_date': row[6]} for row in rows]
