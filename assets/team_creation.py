import requests
url = "https://pokeapi.co/api/v2"

def getTeam() -> dict:
    team = {}
    while True:
        team_size = input("How many Pokemon do you want on your team (max 6)?: ")
        while not team_size.isdigit():
            team_size = input("Error. Please input a number between 1 and 6: ")

        team_size = int(team_size)
        if team_size >= 1 and team_size <= 6:
            break
        print("Error, you need to have at least one and no more than six!")
    team["pokemon"] = []
    print("\n~~~ CHOOSE YOUR POKEMON ~~~\n")

    for i in range(0, team_size):
        pokemon = input(f"Enter your choice for Pokemon #{i+1} (you can enter the name or Pokedex #): ")
    
        try:
            response = requests.get(f"{url}/pokemon/{pokemon}", timeout = 10)
    
            if response.status_code == 200:
                team["pokemon"].append(response.json()["name"])
            else:
                print(f"Invalid pokemon name: {pokemon}. Pokemon not added")
    
        except requests.exceptions.Timeout:
            print("Request timed out")
        except requests.exceptions.RequestException as e:
            print("Requested failed: ", e)
    
    if len(team) > 0:
        print(f"Here is your team: {team["pokemon"]}")
    else:
        print("No pokemon were added to the team!")
        return 
    
    print("Great! Now, what is your team name?")
    team["team_name"] = "" 
    
    # get team name and ensure it is alphanumeric. also make sure the name is not too long
    while True:
        team["team_name"]= input("Enter your team name: ")
        if len(team["team_name"]) <= 30:
            break
        print("Error, team name too long or special characters used. Try again.")

    return team