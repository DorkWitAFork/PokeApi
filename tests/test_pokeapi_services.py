import pytest
import requests
from services.pokeapi_services import PokeApiRequestError, PokeApiResponseError, lookup_pokemon
from unittest.mock import patch, Mock

from services.pokeapi_services import lookup_pokemon
from models.Pokemon import Pokemon

@patch("services.pokeapi_services.requests.get")
def test_lookup_valid_pokemon(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "pikachu", "id": 25, 
                                       "moves": [{
                                           "move": {"name": "thunder-shock"}
                                           }],
                                       }

    mock_get.return_value = mock_response

    pokemon = lookup_pokemon("pikachu")

    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == "pikachu"
    assert pokemon.pokedex_id == 25

@patch("services.pokeapi_services.requests.get")
def test_lookup_invalid_pokmeon(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    pokemon = lookup_pokemon("not-a-pokemon")

    assert pokemon is None

@patch("services.pokeapi_services.requests.get")
def test_lookup_timeout_raises_request_error(mock_get):
    mock_get.side_effect = requests.Timeout("Request timed out")

    with pytest.raises(PokeApiRequestError):
        lookup_pokemon("pikachu")

@patch("services.pokeapi_services.requests.get")
def test_lookup_malformed_response(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "pikachu", "id": 25,}
    mock_get.return_value = mock_response

    with pytest.raises(PokeApiResponseError):
        lookup_pokemon("pikachu")

@patch("services.pokeapi_services.requests.get")
def test_lookup_with_500_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("500 Server Error")
    )
    mock_get.return_value = mock_response

    with pytest.raises(PokeApiRequestError):
        lookup_pokemon("pikachu")