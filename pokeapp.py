from workflows.team_creation import *
from workflows.player_setup import *
from workflows.pokemon_actions import *
from models.Pokemon import Pokemon
from models.Team import Team

def main():

    print("\nWelcome to the Pokemon Team Builder!")
    print("-------------------------------------\n")

    player = get_new_player()
    team = get_new_team()    

    print(f"\nAwesome! So your team name is {team.get_name()}!")

    save = ""
    while save.upper() != "Y" and save.upper() != "N":
        save = input("Do you want to save this team for later? (Y/N) -> ")
    print("Cool, we got out of that.\n")

    print("Testing some Pokemon stuff")
    print(f"Team: {team.get_pokemon_names()}")
    test_pokemon = team.get_team()[0]
    print(f"Pokemon test name: {test_pokemon.get_name()}")
    print("Let's test adding a move")
    for i in range(5):
        choose_move_for_pokemon(test_pokemon)


if __name__ == '__main__':
    main()
