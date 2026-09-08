import requests

url = "https://pokeapi.co/api/v2"

response = requests.get(url)

print(f"Status code: {response.status_code}")
print(f"Content Type: {response.headers.get("Content-Type")}")

data = response.json()
print(data)