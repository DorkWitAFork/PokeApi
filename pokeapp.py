import requests

from assets.team_creation import *

def main():

    print("Welcome to the Pokemon Team Builder!")
    print("-------------------------------------\n")

    
    # Build the team by inputting names of pokemon, which are then looked up.
    team = get_new_team()    

    print(f"\nAwesome! So your team name is {team.getName()}!")

    print("Wait, what's YOUR name?!")
    trainer_name = input("Tell me your name! -> ")
    print(f"\nGreat, nice to meet you {trainer_name}!")

    save = ""
    while save.upper() != "Y" and save.upper() != "N":
        save = input("Do you want to save this team for later? (Y/N) -> ")
    print("Cool, we got out of that.\n")



if __name__ == '__main__':
    main()



# data = response.json()
# print(data["name"])