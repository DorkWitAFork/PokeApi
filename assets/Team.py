class Team():
    def __init__(self):
        self.name = ""
        self.pokemon = []
        self.size = 0

    def getName(self):
        return self.name

    def getTeam(self):
        return self.pokemon

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def setName(self, name):
        self.name = name

    def addPokemon(self, pokemon):
        if self.size >= 6:
            print("Cannot add any pokemon. Team full!")
            return
        self.pokemon.append(pokemon)
        self.size += 1

    def deletePokemon(self, pokemon):
        if pokemon not in self.pokemon:
            print("Error. Pokemon not on team.")
            return
        self.pokemon.remove(pokemon)
        self.size -= 1
