import requests

from models.Pokemon import Pokemon

BASE_URL = "https://pokeapi.co/api/v2"

def lookup_pokemon(identifier: str) -> Pokemon | None:
    try:
        response = requests.get(f"{BASE_URL}/pokemon/{identifier}", timeout=10)

        if response.status_code == 404:
            return None

        response.raise_for_status()
    except requests.RequestException as error:
        raise PokeApiRequestError("Could not complete the PokeAPI request.") from error

    try:
        data = response.json()
        learnable_moves = {move_entry["move"]["name"] for move_entry in data["moves"]}

        pokemon = Pokemon(data["name"],data["id"], learnable_moves)
        return pokemon
    except (KeyError, TypeError, ValueError) as error:
        raise PokeApiResponseError("PokeAPI returned an excepted response.") from error

class PokeApiError(RuntimeError):
    pass

class PokeApiRequestError(PokeApiError):
    pass

class PokeApiResponseError(PokeApiError):
    pass