import sqlite3


conn = sqlite3.connect(
    "documents.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    upload_time TEXT,

    total_chunks INTEGER
)
""")

conn.commit()


def save_document_metadata(
    filename,
    upload_time,
    total_chunks
):

    cursor.execute("""
    INSERT INTO documents (
        filename,
        upload_time,
        total_chunks
    )
    VALUES (?, ?, ?)
    """, (
        filename,
        upload_time,
        total_chunks
    ))

    conn.commit()


def get_all_documents():

    cursor.execute("""
    SELECT * FROM documents
    """)

    rows = cursor.fetchall()

    documents = []

    for row in rows:

        documents.append({
            "id": row[0],
            "filename": row[1],
            "upload_time": row[2],
            "total_chunks": row[3]
        })

    return documents