import numpy as np

def is_positive_integer(num: int | float) -> bool:
    return type(num) in [int, float] and num > 0

class Raffle:
    def __init__(self, ticket_price: float, max_num_of_tickets_per_person: int = 5, max_num_of_people: int = 10, available_ticket_for_sale = 100):
        if not is_positive_integer(ticket_price):
            raise ValueError("Ticket_price should be a positive integer number")
        if not is_positive_integer(max_num_of_tickets_per_person):
            raise ValueError("Max number of tickets per person should be a positive integer number")
        if not is_positive_integer(max_num_of_people):
            raise ValueError("Max number of participants should be a positive integer number")
        if not is_positive_integer(available_ticket_for_sale):
            raise ValueError("Total number of available tickets should be a positive integer number")
        self._participants: dict = dict()
        self._ticket_price = ticket_price
        self._total_earnings = 0
        self._max_tickets = max_num_of_tickets_per_person
        self._max_people = max_num_of_people
        self._available_tickets = available_ticket_for_sale
        pass
    
    def sell_tickets(self, name, quantity) -> bool:
        if name in self._participants:
            # make sure that participant did not reach max tickets per person
            if (self._participants[name] + quantity) > self._max_tickets:
                raise ValueError(f"Can't sell more than {self._max_tickets} to {name}")
        # make sure that raffle did not reach max num of participants already
        elif len(self._participants) >= self._max_people:
            raise ValueError(f"You can't sell to more people, the max of {self._max_people} has been reached")
        elif quantity > self._max_tickets:
            raise ValueError(f"Max num of tickets per person is {self._max_tickets}")


        self._participants[name] = self._participants.get(name, 0) + quantity
        self._total_earnings += quantity * self._ticket_price
        self._available_tickets -= quantity
        return True
    
    def roll(self, num_of_winners: int = 3) -> list[str]:
        if not is_positive_integer(num_of_winners):
            raise ValueError("Number of winners should be a positive integer")
        if len(self._participants) <= 0:
            raise Exception("There are no participants!")
        names = list(self._participants)
        weights = list(self._participants.values())
        sum_weights = sum(weights)
        weights_normalized = [w/sum_weights for w in weights]
        winners = list(np.random.choice(names, size=num_of_winners, replace=False, p=weights_normalized))
        return winners
    
    def get_profit(self) -> float:
        return self._total_earnings
    
    def get_number_available_tickets(self) -> float:
        return self._available_tickets
    