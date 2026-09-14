from assets.Team import Team
from assets.Pokemon import Pokemon

def test_new_team_is_empty():
    team = Team()

    assert team.get_size() == 0

def test_add_pokemon_to_team():
    team = Team()
    pokemon = Pokemon("pikachu", 25)

    team.add_pokemon(pokemon)

    assert pokemon in team.get_team()
    assert team.get_size() == 1