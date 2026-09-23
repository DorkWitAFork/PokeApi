from database.connection import get_connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS players ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL 
            )
        """)