from models.Team import Team
from models.Pokemon import Pokemon


def test_new_team_is_empty():
    team = Team()

    assert team.get_size() == 0

def test_add_pokemon_to_team():
    team = Team()
    pokemon = Pokemon("pikachu", 25)

    team.add_pokemon(pokemon)

    assert pokemon in team.get_team()
    assert team.get_size() == 1

def test_team_more_than_six():
    team = Team()

    for number in range(6):
        pokemon = Pokemon(f"pokemon-{number}", number)
        team.add_pokemon(pokemon)

    extra_pokemon = Pokemon("extra", 999)
    team.add_pokemon(extra_pokemon)

    assert team.get_size() == 6
    assert extra_pokemon not in team.get_team()

def test_delete_pokemon_from_team():
    team = Team()
    pokemon = Pokemon("pikachu", 25)

    team.add_pokemon(pokemon)

    team.delete_pokemon(pokemon)

    assert pokemon not in team.get_team()
    assert team.get_size() == 0

def test_delete_not_affect_team():
    team = Team()
    pokemon1 = Pokemon("pikachu", 25)
    pokemon2 = Pokemon("bulbasaur", 1)

    team.add_pokemon(pokemon1)

    team.delete_pokemon(pokemon2)

    assert team.get_size() == 1