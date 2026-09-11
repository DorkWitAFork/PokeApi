class Team():
    def __init__(self):
        self.name = ""
        self.pokemon = []

    def getName(self):
        return self.name

    def getTeam(self):
        return self.pokemon

    def getSize(self):
        return len(self.pokemon)

    def setName(self, name):
        self.name = name

    def addPokemon(self, pokemon):
        if self.getSize() >= 6:
            print("Cannot add any pokemon. Team full!")
            return
        self.pokemon.append(pokemon)

    def deletePokemon(self, pokemon):
        if pokemon not in self.pokemon:
            print("Error. Pokemon not on team.")
            return
        self.pokemon.remove(pokemon)
