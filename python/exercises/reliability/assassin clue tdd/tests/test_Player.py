import pytest
from components.Player import *

visited_places = ["p1", "p2", "p3"]
weapons = ["w1", "w2", "w3", "w4"]

@pytest.fixture
def good_player() -> Player:
    return Player("test player", False, visited_places, weapons)

def test_shows_list_visited_places(good_player: Player) -> None:
    data = good_player.show_some_places_and_weapons()
    assert type(data) == list
    assert type(data[0]) == list
    assert len(data[0]) == 2
    assert data[0][0] in visited_places
    
def test_shows_one_fav_weapon(good_player: Player) -> None:
    data = good_player.show_some_places_and_weapons()
    assert type(data[1]) == list
    assert len(data[1]) == 1
    assert data[1][0] in weapons


def test_fail_if_visited_places_empty() -> None:
    with pytest.raises(Exception):
        Player("test player", False, [], weapons) 

def test_fail_if_fav_weapons_empty() -> None:
    with pytest.raises(Exception):
        Player("test player", False, visited_places, []) 

def test_fail_if_name_empty() -> None:
    with pytest.raises(Exception):
        Player("", False, visited_places, weapons) 