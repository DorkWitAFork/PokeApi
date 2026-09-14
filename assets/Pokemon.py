class Pokemon():
    def __init__(self, name, pokedex_id):
        self.name = name
        self.pokedex_id = pokedex_id
        self.moves = [] 

    def add_move(self, move):
        # check if the move is learnable for that pokemon
        # send an error if the move is not learnable.
        if len(self.moves) < 4:
            # add the move
            return
        # return an error if there is no room for the move.
        # perhaps we can ask the user if they want to delete a move or cancel the add move entirely.
    
    def delete_move(self, move):
        # check that the move is in the list of moves for the Pokemon
        if move in self.moves:
            self.moves.remove(move)
            return
        # send an error telling the user that the pokemon does not know that move
