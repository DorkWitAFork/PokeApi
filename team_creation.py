from models.Team import Team 
from services.pokeapi_services import *

url = "https://pokeapi.co/api/v2"

def get_new_team() -> Team:
    newTeam = Team()

    print("\n~~~ CHOOSE YOUR POKEMON ~~~\n")

    team_size = get_team_size()
    newTeam = choose_pokemon(newTeam, team_size)
    print(f"Current team: {newTeam.get_pokemon_names()}")
    newTeam = choose_team_name(newTeam)
       
    return newTeam

def get_team_size() -> int:
    while True:
            team_size = input("How many Pokemon do you want on your team (max 6)?: ")
            while not team_size.isdigit():
                team_size = input("Error. Please input a number between 1 and 6: ")
            team_size = int(team_size)
            if team_size >= 1 and team_size <= 6:
                break
            print("Error, you need to have at least one and no more than six!")
    return team_size

def choose_pokemon(team : Team, n : int) -> Team:
    for i in range(0, n):
        choice = str(input(f"Enter your choice for Pokemon #{i+1} (you can enter the name or Pokedex #): "))

        pokemon = lookup_pokemon(choice)         

        if pokemon is not None:
            team.add_pokemon(pokemon)
        else:
            print(f"Error adding pokemon: {choice}. Pokemon not added.")

    return team

def choose_team_name(team : Team) -> Team:
    print("Great! Now, what is your team name?")
    name = "" 

    while True:
        name = input("Enter your team name: ")
        if len(name) <= 30:
            break
        print("Error, team name too long or special characters used. Try again.")
    
    team.set_name(name)
    return team