class Raffle:
    def __init__(self, ticket_price: float | int):
        self._participants: dict = dict()
        if type(ticket_price) not in [float, int]:
            raise ValueError
        if ticket_price <= 0:
            raise ValueError
        self._ticket_price = ticket_price
        self._total_earnings = 0
        pass
    
    def sell_tickets(self, name, quantity) -> bool:
        self._participants[name] = quantity
        self._total_earnings += quantity * self._ticket_price
        return True
    
    def roll(self) -> list[str]:
        return [""]
    
    def get_profit(self) -> float:
        return self._total_earnings
    