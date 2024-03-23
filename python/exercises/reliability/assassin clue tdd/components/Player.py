import random
from plugins import readers as r
from typing import Type
import pathlib

RESOURCES_FOLDER = "resources"

class Player:
    def __init__(self, name: str,list_visited_places: list, list_fav_weapons: list):
        if len(name) == 0: raise Exception("Name should not be empty")
        self.name = name
        if len(list_visited_places) == 0: raise Exception("List of visited places should not be empty")
        if len(list_visited_places) > 3: raise Exception("List of visited places should not > 3")
        self.list_visited_places = list_visited_places

        if len(list_fav_weapons) == 0: raise Exception("List of fav weapons should not be empty")
        if len(list_fav_weapons) > 2: raise Exception("List of fav weapons should not be > 2")
        self.list_fav_weapons = list_fav_weapons

        self.is_dead = False
        self.is_murderer = False
    
    def show_some_places_and_weapons(self) -> list[list]:
        if len(self.list_visited_places) > 2:
            places = random.sample(self.list_visited_places, 2)
        else:
            places = self.list_visited_places
        weapon = random.sample(self.list_fav_weapons, 1)
        return [places, weapon]
    
    def _die(self):
        if not self.is_murderer:
            print(f"{self.name} has been killed!!")
            self.is_dead = True
        else:
            raise Exception(f"{self.name} is the killer! they can't die")

    def kill(self, player):
        if self.is_murderer:
            player._die()
            return player
        else:
            raise Exception(f"{self.name} is not a murderer! they can't kill another player.")
    
    def _set_as_murderer(self):
        if not self.is_murderer:
            self.is_murderer = True
        else:
            raise Exception(f"{self.name} is already set as the murderer")
        

def import_places(folder_name = RESOURCES_FOLDER, file_name = "places.json"):
    file_path = pathlib.Path(f"./{folder_name}/{file_name}")
    data = r.json(file_path)
    return list(data["places"])

def import_weapons(folder_name = RESOURCES_FOLDER, file_name = "weapons.json"):
    file_path = pathlib.Path(f"./{folder_name}/{file_name}")
    data = r.json(file_path)
    return list(data["weapons"])

def import_bot_names(folder_name = RESOURCES_FOLDER, file_name = "bots.json"):
    file_path = pathlib.Path(f"./{folder_name}/{file_name}")
    data = r.json(file_path)
    return list(data["bots"])

def get_n_random_items_from_list(the_list, n: int) -> list[str]:
    return random.sample(the_list, n)
    
def get_one_random_item(the_list) -> str:
    return random.choice(the_list)

def reset(players):
    for player in players:
        player.is_murderer = False
        player.is_dead = False

def random_players_creator(n, Player: Type[Player]) -> list[Player]:
    players_list = []
    random_names_list = get_n_random_items_from_list(import_bot_names(), n)

    for _ in range(n):
        players_list.append(Player(random_names_list.pop(), get_n_random_items_from_list(import_places(), 3), get_n_random_items_from_list(import_weapons(), 2)))

    return players_list

def set_random_murderer(players_list: list[Player]):
    killer = random.choice(players_list)
    killer.is_murderer = True
    return killer

def get_a_random_place_from_player(player: Player) -> str:
    return random.choice(player.list_visited_places)

def kill_random_player(players, killer):
    innocents = [player for player in players if player.is_murderer == False]
    killer.kill(random.choice(innocents))

def filter_alive_players(players: list[Player]) -> list:
    return [alive_player for alive_player in players if alive_player.is_dead == False]

def get_player_by_num(player_num: int, players_list: list[Player]):
    # player_num is not the index, it's index-1
    # validate:
    if player_num > len(players_list) or player_num < 1:
        print(f"Please put a number between 1 - {len(players_list)}")
        print(f"{player_num} - {len(players_list)}")
        raise Exception("wrong input") # TODO: handle it
    return players_list[player_num-1]