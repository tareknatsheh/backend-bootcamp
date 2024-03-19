import random

class Player:
    def __init__(self, name: str, is_murderer: bool, list_visited_places: list, list_fav_weapons: list):
        if len(name) == 0: raise Exception("Name should not be empty")
        self.name = name
        self.is_murderer = is_murderer
        if len(list_visited_places) == 0: raise Exception("List of visited places should not be empty")
        self.list_visited_places = list_visited_places
        if len(list_fav_weapons) == 0: raise Exception("List of fav weapons should not be empty")
        self.list_fav_weapons = list_fav_weapons
    
    def show_some_places_and_weapon(self) -> list[list]:
        if len(self.list_visited_places) > 2:
            places = random.sample(self.list_visited_places, 2)
        else:
            places = self.list_visited_places
        weapon = random.sample(self.list_fav_weapons, 1)
        return [places, weapon]