from database.connection import get_connection
from models.Team import Team

def save_team(team: Team, player_id: int) -> int:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO teams (player_id, name)
            VALUES (?, ?)
            """,
            (player_id, team.get_name())
        )

        team_id = cursor.lastrowid

        for slot, pokemon in enumerate(team.get_team(), start=1):
            connection.execute(
                """
                INSERT INTO team_pokemon (team_id, name, pokedex_id, slot)
                VALUES (?, ?, ?, ?)
                """,
                (team_id, pokemon.get_name(), pokemon.get_pokedex_id(), slot)
            )

        return team_id
            
