import requests
def main():
    url = "https://pokeapi.co/api/v2"

    print("Welcome to the Pokemon Team Builder!")
    print("-------------------------------------\n")


    while True:
        team_size = input("How many Pokemon do you want on your team (max 6)?: ")
        while not team_size.isdigit():
            team_size = input("Error. Please input a number between 1 and 6: ")

        team_size = int(team_size)
        if team_size >= 1 and team_size <= 6:
            break
        print("Error, you need to have at least one and no more than six!")

    # Build the team by inputting names of pokemon, which are then looked up.
    team = []
    print("\n~~~ CHOOSE YOUR POKEMON ~~~\n")
    for i in range(0, team_size):
        pokemon = input(f"Enter your choice for Pokemon #{i+1}: ")

        try:
            response = requests.get(f"{url}/pokemon/{pokemon}", timeout = 10)

            if response.status_code == 200:
                team.append(response.json()["name"])
            else:
                print(f"Invalid pokemon name: {pokemon}. Pokemon not added")

        except requests.exceptions.Timeout:
            print("Request timed out")
        except requests.exceptions.RequestException as e:
            print("Requested failed: ", e)

    if len(team) > 0:
        print(f"Here is your team: {team}")
    else:
        print("No pokemon were added to the team!")
        return 

if __name__ == '__main--':
    main()



# data = response.json()
# print(data["name"])