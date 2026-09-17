from models.Player import Player

# NEW PLAYER FUNCTIONS
def get_new_player():

    name = get_new_name()
    player = Player(name)

    return player

# For new players without an assigned name yet.
def get_new_name():
    print("Wait, what's your name?")
    while True:
        name = input("Tell me your name! -> ")
        if len(name) <= 30:
            break
        print("Error, name too long.")

    print(f"Great, nice to meet you, {name}!")
    return name

# CURRENT PLAYER FUNCTIONS
# Not for new players. Update name for current player.
def update_player_name():
    pass