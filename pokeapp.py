import sqlite3
from database.schema import initialize_database
from database.repositories.player_repository import save_player
from workflows.team_creation import *
from workflows.player_setup import *
from workflows.pokemon_actions import *
from models.Team import Team

def main():

    try:
        initialize_database()
    except sqlite3.Error as error:
        print(f"Could not initialize the database: {error}")
        return
              
    print("\nWelcome to the Pokemon Team Builder!")
    print("-------------------------------------\n")

    player = get_new_player()
    team = get_new_team()    

    print(f"\nAwesome! So your team name is {team.get_name()}!")

    save = ""
    while save.upper() != "Y" and save.upper() != "N":
        save = input("Do you want to save this team for later? (Y/N) -> ").strip()

    if save.upper() == "Y":
        try:
            player_id = save_player(player)
            print(f"Player saved successfully with ID {player_id}")
        except sqlite3.Error as error:
            print(f"Could not save player: {error}")

    else:
        print("Player not saved.")

if __name__ == '__main__':
    main()

