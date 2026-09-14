from assets.Team import Team

class Player():

    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team: Team):
        self.teams.append(team)
        # print a success message
        return True

    def delete_team(self, team: Team):
        if team in self.teams:
            self.teams.remove(team)
            return True
        # send an error that the team was unavailable. 
        return False