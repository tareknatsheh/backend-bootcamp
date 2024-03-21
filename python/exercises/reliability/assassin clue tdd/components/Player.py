import random

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