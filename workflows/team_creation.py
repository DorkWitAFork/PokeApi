from models.Team import Team 
from services.pokeapi_services import PokeApiError, lookup_pokemon 

def get_new_team() -> Team:
    new_team = Team()

    print("\n~~~ CHOOSE YOUR POKEMON ~~~\n")

    team_size = get_team_size()
    new_team = choose_pokemon(new_team, team_size)
    print(f"Current team: {new_team.get_pokemon_names()}")
    new_team = choose_team_name(new_team)
       
    return new_team 

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

def choose_pokemon(team: Team, n: int) -> Team:
    i = 0
    while i < n:
        choice = str(input(f"Enter your choice for Pokemon #{i+1} (you can enter the name or Pokedex #): ")).strip().lower()
        try:
            pokemon = lookup_pokemon(choice)
        except PokeApiError as error:
            print(f"\nUnable to look up {choice}: {error}")

        if pokemon is None:
            print(f"Pokemon '{choice}' was not found. Try again.")
            continue
        team.add_pokemon(pokemon)
        i += 1
    return team

def choose_team_name(team: Team) -> Team:
    print("Great! Now, what is your team name?")
    name = "" 

    while True:
        name = input("Enter your team name: ")
        if len(name) <= 30:
            break
        print("Error, team name too long or special characters used. Try again.")
    
    team.set_name(name)
    return team

class TeamCreationCancelled(Exception):
    pass