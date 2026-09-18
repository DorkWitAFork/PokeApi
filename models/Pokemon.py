class Pokemon():
    def __init__(self, name, pokedex_id, learnable_moves=None):
        self.name = name
        self.pokedex_id = pokedex_id
        self.learnable_moves = learnable_moves or set()
        self.moves = [] 

    def add_move(self, move) -> bool:
        if not self.move_is_learnable(move):
            return False

        if move in self.moves:
            return False
        
        if len(self.moves) >= 4:
            return False 

        self.moves.append(move)
        return True

    def delete_move(self, move) -> bool:
        if move not in self.moves:
            return False 

        self.moves.remove(move)
        return True 

    def replace_move(self, old_move, new_move) -> bool:
        if old_move not in self.moves:
            return False

        if not self.move_is_learnable(new_move):
            return False

        if new_move in self.moves:
            return False

        index = self.moves.index(old_move)
        self.moves[index] = new_move
        return True  

    def move_is_learnable(self, move) -> bool:
        return move in self.learnable_moves 

    def get_moves(self):
        return self.moves.copy()

    def get_name(self):
        return self.name