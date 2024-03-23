class Raffle:
    def __init__(self, ticket_price: float, max_num_of_tickets_per_person: int = 5):
        self._participants: dict = dict()
        if type(ticket_price) not in [float, int] or ticket_price <= 0:
            raise ValueError
        self._ticket_price = ticket_price
        self._total_earnings = 0
        self._max_tickets = max_num_of_tickets_per_person
        pass
    
    def sell_tickets(self, name, quantity) -> bool:
        if name in self._participants:
            if (self._participants[name] + quantity) > self._max_tickets:
                raise ValueError(f"Can't sell more than {self._max_tickets} to {name}")
        self._participants[name] = quantity
        self._total_earnings += quantity * self._ticket_price
        return True
    
    def roll(self) -> list[str]:
        return [""]
    
    def get_profit(self) -> float:
        return self._total_earnings
    