import requests

url = "https://pokeapi.co/api/v2"

print("Welcome to the Pokemon Team Builder!")
print("-------------------------------------\n\n")

while True:
    team_size = int(input("How many Pokemon do you want on your team (max 6)?: "))
    if team_size >= 1 and team_size <= 6:
        break
    print("Error, you need to have at least one and no more than six!")
for i in range(1, team_size+1):
    print(i)

pokemon = input("Enter a pokemon you'd like to see: ")


try:
    response = requests.get(f"{url}/pokemon/{pokemon}", timeout = 10)
    print("Final url: ", response.url)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Request failed: ", e)



print(f"Status code: {response.status_code}")
print(f"Content Type: {response.headers.get("Content-Type")}")

data = response.json()
print(data["name"])