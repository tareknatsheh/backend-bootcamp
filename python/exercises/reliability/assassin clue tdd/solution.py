"""
Clue Assassin usin TDD

Basic components:
Player class:
    parameters:
        name, is_murderer, list of visited places, list of fav weapons
    methods:
        randomly show 2 visited places and 1 fav weapon
            return example [["p1", "p2"], ["w1"]]

Basic actions:
1) accuse:
    parameters:
        - player
    returns:
        - True or False

2) suspect:
    parameters:
        - player
    returns:
        - list of some of visited places and another list of some fav weapons

3) kill:
    parameters:
        - list of all alive players
    returns:
        - new list of alive players (will be missing the victim)


"""

from importlib import import_module
import os

def list_of_all_actions() -> list:
    all_available_plugins = os.listdir(f"./actions")
    all_modules_plugins_names = [f.replace(".py","") for f in all_available_plugins if f.endswith('.py') and not f.startswith("__")]
    modules_list = []
    for action_name in all_modules_plugins_names:
        module = import_module(f"actions.{action_name}")
        modules_list.append(module)
    return modules_list

all_actions = list_of_all_actions()
for action in all_actions:
    print(action.get_name())