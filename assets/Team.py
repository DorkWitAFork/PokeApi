class Team():
    def __init__(self):
        self.name = ""
        self.pokemon = []

    def get_name(self):
        return self.name

    def get_team(self):
        return self.pokemon

    def get_size(self):
        return len(self.pokemon)

    def set_name(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if self.get_size() >= 6:
            print("Cannot add any pokemon. Team full!")
            return
        self.pokemon.append(pokemon)

    def delete_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            print("Error. Pokemon not on team.")
            return
        self.pokemon.remove(pokemon)
