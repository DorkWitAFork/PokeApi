from models.Pokemon import Pokemon

# function to validate and create a new pokemon
# this would get called when trying to add a pokemon to the team.
# 

# functions to validate moves
def choose_move_for_pokemon(pokemon) -> bool:
    move = input("Which move should it learn? ").strip().lower()

    if pokemon.add_move(move):
        print(f"{pokemon.get_name()} learned {move}!")
        return True

    print(f"{pokemon.get_name()} could not learn {move}.")
    return False