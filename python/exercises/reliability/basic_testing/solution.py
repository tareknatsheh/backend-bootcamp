from Raffle import Raffle

the_raffle = Raffle(3.4, 10)
# the_raffle.sell_tickets("user0", 1)
# the_raffle.sell_tickets("user1", 3)
# the_raffle.sell_tickets("user2", 3)
# the_raffle.sell_tickets("user3", 10)
# the_raffle.sell_tickets("user4", 2)


winners = the_raffle.roll()

print("Winners of the Lottery are:")
for index, person in enumerate(winners):
    print(f"{index+1}) {person}")