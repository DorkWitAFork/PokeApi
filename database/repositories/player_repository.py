from database.connection import get_connection
from models.Player import Player

def save_player(player: Player) -> int:
    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO PLAYERS (name) VALUES (?)""",
            (player.get_name(),)
        )

    player.id = cursor.lastrowid
    return cursor.lastrowid