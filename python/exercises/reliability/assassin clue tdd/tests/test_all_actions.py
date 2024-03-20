"""
Actions are built as plugins, therefore the plugin system expects some
basic methods that all and each one of them should have.
"""
import os
from importlib import import_module


def list_of_all_actions() -> list:
    all_available_plugins = os.listdir(f"./actions")
    all_modules_plugins_names = [f.replace(".py","") for f in all_available_plugins if f.endswith('.py') and not f.startswith("__")]
    modules_list = []
    for action_name in all_modules_plugins_names:
        module = import_module(f"actions.{action_name}")
        modules_list.append(module)
    return modules_list



def test_all_actions_has_get_name():
    all_actions = list_of_all_actions()
    for action in all_actions:
        assert hasattr(action, 'get_name'), f"The plugin {action} does not have a 'get_name' method"
        assert callable(action.get_name), f"The attribute 'get_name' in {action} is not callable"