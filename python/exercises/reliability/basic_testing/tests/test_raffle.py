import pytest
from Raffle import Raffle


def test_creating_raffle_object_with_str_parameter() -> None:
    with pytest.raises(ValueError):
        Raffle("some text")

def test_creating_raffle_object_with_negative_ticket_price() -> None:
    with pytest.raises(ValueError):
        Raffle(-5)


TESTING_TICKET_PRICE = 3.4
@pytest.fixture()
def my_raffle():
    return Raffle(TESTING_TICKET_PRICE)

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

