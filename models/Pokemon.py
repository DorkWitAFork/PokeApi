class Pokemon():
    def __init__(self, name, pokedex_id, learnable_moves=None):
        self.name = name
        self.pokedex_id = pokedex_id
        self.learnable_moves = learnable_moves or set()
        self.moves = [] 

    def add_move(self, move) -> bool:
        if move not in self.learnable_moves:
            print(f"Error, {self.name} cannot learn {move}!")
            return False

        if len(self.moves) < 4:
            # add the move
            self.moves.append(move)
            return True

        print(f"Oops, {self.name} already knows four moves! Do you want to replace an old move?")
        new_move_choice = ""
        while new_move_choice.upper() != "Y" and new_move_choice.upper() != "N":
            new_move_choice = input("(Y/N) -> ")

        if new_move_choice.upper() == "N":
            return False

        move_to_delete = input(f"Which move do you want to replace? {self.get_moves()}\n -> ")

        if move_to_delete in self.moves:
            self.delete_move(move)
            self.moves.append(move)
            return True            
        
    
    def delete_move(self, move):
        # check that the move is in the list of moves for the Pokemon
        if move in self.moves:
            self.moves.remove(move)
            return
        # send an error telling the user that the pokemon does not know that move

    def get_moves(self):
        return self.moves