from models.Player import Player
from models.Team   import Team

def test_add_team_to_player():
    player = Player("Spencer")
    team = Team()

    result = player.add_team(team)

    assert result is True
    assert team in player.teams
    assert len(player.teams) == 1

def test_delete_team_from_player():
    player = Player("Spencer")
    team = Team()

    player.add_team(team)

    result = player.delete_team(team)

    assert team not in player.teams
    assert result is True
    assert len(player.teams) == 0

def test_delete_team_not_in_player():
    player = Player("Spencer")
    team = Team()

    result = player.delete_team(team)

    assert result is False
    assert player.teams == []