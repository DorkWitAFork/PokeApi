import requests

from models.Pokemon import Pokemon

BASE_URL = "https://pokeapi.co/api/v2"

def lookup_pokemon(identifier) -> Pokemon | None:
    response = requests.get(f"{BASE_URL}/pokemon/{identifier}", timeout=10)

    if response.status_code == 404:
        return None

    response.raise_for_status()

    data = response.json()

    learnable_moves = {move_entry["move"]["name"] for move_entry in data["moves"]}

    pokemon = Pokemon(data["name"],data["id"], learnable_moves)

    return pokemon
