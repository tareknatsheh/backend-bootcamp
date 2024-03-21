import random

def reset(players):
    for player in players:
        player.is_murderer = False
        player.is_dead = False

def players_creator(n, Player):
    p1 = Player("Will Smith", ["Jerusalem","Ramallah","Haifa"], ["Revolver", "Candlestick"])
    p2 = Player("John Wick", ["Glenview","Brookside","Maplewood"], ["Wrench", "Candlestick"])
    p3 = Player("Hosam", ["Greenfield", "Riverdale", "Lakeview"], ["Sword", "Dagger"])
    p4 = Player("Goku", ["Clearwater", "Meadowbrook", "Fairview"], ["Wrench", "Revolver"])

    alive_players = [p1, p2, p3, p4]
    return alive_players

def set_random_murderer(players_list: list):
    killer = random.choice(players_list)
    killer.is_murderer = True
    return killer

def get_a_random_place_from_player(player) -> str:
    return random.choice(player.list_visited_places)

def kill_random_player(players, killer):
    innocents = [player for player in players if player.is_murderer == False]
    killer.kill(random.choice(innocents))

def investigate_suspect(player_num, alive_players):
    # validate:
    if player_num > len(alive_players) or player_num < 1:
        print(f"Please put a number between 1 - {len(alive_players)}")
        raise Exception("wrong input") # TODO: handle it
    else:
        # If suspect: see 2 visited places and 1 fav weapon randomly
        chosen_suspect_index = player_num - 1
        suspect = alive_players[chosen_suspect_index]
        some_visited_places = random.sample(suspect.list_visited_places, 2)
        one_of_fav_weapons = random.choice(suspect.list_fav_weapons)

        print(f"{suspect.name} have visited the following places:")
        for place in some_visited_places:
            print(place)
        print(f"One of {suspect.name} fav weapons is **{one_of_fav_weapons}**")

def list_names(players):
    print("\nHere are the other players:")
    for index, player in enumerate(players):
        print(f"{index + 1}) {player.name}")

def filter_alive_players(players: list) -> list:
    return [alive_player for alive_player in players if alive_player.is_dead == False]

def get_player_by_num(player_num, players_list):
    # player_num is not the index, it's index-1
    # validate:
    if player_num > len(players_list) or player_num < 1:
        print(f"Please put a number between 1 - {len(players_list)}")
        print(f"{player_num} - {len(players_list)}")
        raise Exception("wrong input") # TODO: handle it
    return players_list[player_num-1]

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

def do_you_want_to_play_again() -> bool:
    user_answer = input("Do you want to play again? (y/n)\n").lower()
    return user_answer == "y"

def accuse(alive_players) -> tuple:
    accused_player_num = int(input(f"Who do you accuse?\nPlease put a number between 1 - {len(alive_players)}\n"))
    accused_player = get_player_by_num(accused_player_num, alive_players)

    return accused_player.is_murderer, accused_player