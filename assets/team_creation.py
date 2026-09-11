import requests

from assets.Team import *

url = "https://pokeapi.co/api/v2"

def getNewTeam() -> Team:
    newTeam = Team()

    print("\n~~~ CHOOSE YOUR POKEMON ~~~\n")

    team_size = getTeamSize()
    team = choosePokemon(team, team_size)
    team = chooseTeamName(team)
        
    return newTeam

def getTeamSize() -> int:
    while True:
            team_size = input("How many Pokemon do you want on your team (max 6)?: ")
            while not team_size.isdigit():
                team_size = input("Error. Please input a number between 1 and 6: ")
            team_size = int(team_size)
            if team_size >= 1 and team_size <= 6:
                break
            print("Error, you need to have at least one and no more than six!")
    return team_size

def choosePokemon(team : Team, n : int) -> Team:
    for i in range(0, n):
        pokemon = str(input(f"Enter your choice for Pokemon #{i+1} (you can enter the name or Pokedex #): "))
            
        try:
            response = requests.get(f"{url}/pokemon/{pokemon}", timeout = 10)
        
            if response.ok:
                team.addPokemon(response.json()["name"])
            else:
                print(f"Error adding pokemon: {pokemon}. Pokemon not added")
        
        except requests.exceptions.Timeout:
            print("Request timed out")
        except requests.exceptions.RequestException as e:
            print("Requested failed: ", e)

def chooseTeamName(team : Team) -> Team:
    print("Great! Now, what is your team name?")
    name = "" 
        
    # get team name and ensure it is alphanumeric. also make sure the name is not too long
    while True:
        name = input("Enter your team name: ")
        if len(name) <= 30:
            break
        print("Error, team name too long or special characters used. Try again.")
    
    team.setName(name)
    return team