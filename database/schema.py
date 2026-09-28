from database.connection import get_connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS players ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL 
            )
        """)

        connection.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players(id)
            )
        """)

        connection.execute("""
        CREATE TABLE IF NOT EXISTS team_pokemon ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            pokedex_id INTEGER NOT NULL,
            slot INTEGER NOT NULL,
            FOREIGN KEY (team_id) REFERENCES teams(id)
            )
        """)