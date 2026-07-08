import sqlite3


def initialize_database():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL,
        report TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()


def save_research(topic, report):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO research_history
        (topic, report)

        VALUES (?, ?)
        """,
        (topic, report)
    )

    conn.commit()
    conn.close()


def get_all_research():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM research_history
        ORDER BY id DESC
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records


def get_research_by_id(record_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM research_history
        WHERE id = ?
        """,
        (record_id,)
    )

    record = cursor.fetchone()

    conn.close()

    return record


def delete_research(record_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM research_history
        WHERE id = ?
        """,
        (record_id,)
    )

    conn.commit()
    conn.close()