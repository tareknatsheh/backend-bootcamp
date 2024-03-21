import random
from components.Player import Player


def investigate_suspect(player_num: int, alive_players: list[Player]):
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


def get_player_by_num(player_num: int, players_list: list[Player]):
    # player_num is not the index, it's index-1
    # validate:
    if player_num > len(players_list) or player_num < 1:
        print(f"Please put a number between 1 - {len(players_list)}")
        print(f"{player_num} - {len(players_list)}")
        raise Exception("wrong input") # TODO: handle it
    return players_list[player_num-1]


def do_you_want_to_play_again() -> bool:
    user_answer = input("Do you want to play again? (y/n)\n").lower()
    return user_answer == "y"

def accuse(alive_players: list[Player]) -> tuple[bool, Player]:
    accused_player_num = int(input(f"Who do you accuse?\nPlease put a number between 1 - {len(alive_players)}\n"))
    accused_player = get_player_by_num(accused_player_num, alive_players)

    return accused_player.is_murderer, accused_player