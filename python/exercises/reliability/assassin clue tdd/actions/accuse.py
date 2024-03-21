from components.Player import Player, get_player_by_num

def get_name():
    return "Accuse a player"

def accuse(alive_players: list[Player]) -> tuple[bool, Player]:
    accused_player_num = int(input(f"Who do you accuse?\nPlease put a number between 1 - {len(alive_players)}\n"))
    accused_player = get_player_by_num(accused_player_num, alive_players)

    return accused_player.is_murderer, accused_player
