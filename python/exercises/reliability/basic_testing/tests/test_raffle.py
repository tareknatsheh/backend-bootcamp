import pytest
from Raffle import Raffle


def test_creating_raffle_object_with_str_parameter() -> None:
    with pytest.raises(ValueError):
        Raffle("some text") # type: ignore

def test_creating_raffle_object_with_negative_ticket_price() -> None:
    with pytest.raises(ValueError):
        Raffle(-5)


TESTING_TICKET_PRICE = 3.4
MAX_NUM_OF_TICKETS = 3
MAX_NUM_OF_PEOPLE = 3
AVAILABLE_TICKETS = 10
@pytest.fixture()
def my_raffle():
    return Raffle(TESTING_TICKET_PRICE, MAX_NUM_OF_TICKETS, MAX_NUM_OF_PEOPLE, AVAILABLE_TICKETS)

def test_creating_raffle_obj_no_profit_at_start(my_raffle: Raffle):
    assert my_raffle.get_profit() == 0

def test_creating_raffle_obj_no_participants_at_start(my_raffle: Raffle):
    assert not my_raffle._participants

def test_selling_a_ticket_adds_to_profit(my_raffle: Raffle):
    my_raffle.sell_tickets("ahmad", 3)
    assert my_raffle.get_profit() == 3 * TESTING_TICKET_PRICE

def test_selling_a_ticket_adds_participants(my_raffle: Raffle):
    my_raffle.sell_tickets("ahmad", 3)
    assert "ahmad" in my_raffle._participants

def test_same_customer_cant_buy_too_much_tickets(my_raffle: Raffle):
    with pytest.raises(ValueError):
        my_raffle.sell_tickets("ahmad", 2)
        my_raffle.sell_tickets("ahmad", 2)
        my_raffle.sell_tickets("ahmad", 2)
        my_raffle.sell_tickets("ahmad", 2)
        my_raffle.sell_tickets("ahmad", 2)

def test_max_num_of_people_that_can_join(my_raffle):
    with pytest.raises(ValueError):
        my_raffle.sell_tickets("user1", 1)
        my_raffle.sell_tickets("user2", 1)
        my_raffle.sell_tickets("user3", 1)
        my_raffle.sell_tickets("user4", 1)

def test_you_can_add_people_up_to_the_max(my_raffle):
    my_raffle.sell_tickets("user1", 3)
    my_raffle.sell_tickets("user2", 3)
    my_raffle.sell_tickets("user3", 3)

    assert len(my_raffle._participants) == 3


def test_available_tickets_for_sale_changes_when_you_sell_some(my_raffle):
    my_raffle.sell_tickets("user1", 3)
    assert my_raffle.get_number_available_tickets() == 7

def test_roll_and_get_winners(my_raffle):
    my_raffle.sell_tickets("user1", 1)
    my_raffle.sell_tickets("user2", 2)
    my_raffle.sell_tickets("user3", 3)

    winners = my_raffle.roll(3)
    assert len(winners) == 3

def test_rolling_without_participants_raises_error(my_raffle):
    with pytest.raises(Exception):
        my_raffle.roll()