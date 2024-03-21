from components.Player import Player

def print_congrats():
    print("\n")
    print("*" * 50)
    print("*" * 6 + " Congrats You Have Catched the Killer " + "*" * 6)
    print("*" * 50)
    print("\n")

def print_welcome():
    print("-" * 30)
    print("----- Assassin Clue Game -----")
    print("-" * 30 + "\n")

def print_game_over():
    print("X" * 13)
    print("**You lost!**")
    print("X" * 13)

def list_names(players: list[Player]):
    print("\nHere are the other players:")
    for index, player in enumerate(players):
        print(f"{index + 1}) {player.name}")
