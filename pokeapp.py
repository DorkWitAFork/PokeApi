import requests

from workflows.team_creation import *
from workflows.player_setup import *

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



if __name__ == '__main__':
    main()
