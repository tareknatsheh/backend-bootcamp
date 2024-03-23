from os import kill
import pytest
from components.Player import *

visited_places = ["p1", "p2", "p3"]
weapons = ["w1", "w2"]

@pytest.fixture
def a_player() -> Player:
    return Player("test player", visited_places, weapons)

def test_shows_list_visited_places(a_player: Player) -> None:
    data = a_player.show_some_places_and_weapons()
    assert type(data) == list
    assert type(data[0]) == list
    assert len(data[0]) == 2
    assert data[0][0] in visited_places
    
def test_shows_one_fav_weapon(a_player: Player) -> None:
    data = a_player.show_some_places_and_weapons()
    assert type(data[1]) == list
    assert len(data[1]) == 1
    assert data[1][0] in weapons


def test_fail_if_visited_places_empty() -> None:
    with pytest.raises(Exception):
        Player("test player", [], weapons) 

def test_fail_if_fav_weapons_empty() -> None:
    with pytest.raises(Exception):
        Player("test player", visited_places, []) 

def test_fail_if_name_empty() -> None:
    with pytest.raises(Exception):
        Player("", visited_places, weapons) 

def test_die(a_player: Player) -> None:
    assert a_player.is_dead == False
    a_player._die()
    assert a_player.is_dead == True
    
def test_innocents_cant_kill(a_player: Player) -> None:
    assert a_player.is_dead == False
    with pytest.raises(Exception):
        innocent_player = Player("TEST N", visited_places, weapons)
        # Let's not ._set_as_murderer()
        innocent_player.kill(a_player)

def test_kill(a_player: Player) -> None:
    assert a_player.is_dead == False
    killer = Player("TEST N", visited_places, weapons)
    killer._set_as_murderer()
    killer.kill(a_player)
    assert a_player.is_dead == True
