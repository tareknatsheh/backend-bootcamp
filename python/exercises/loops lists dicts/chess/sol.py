from random import randint

# Round-robin matches schedule:
# Generates a schedule as a list of zip() objects which is: an iterator of tuples with paired items
def create_schedule(list):
    s = []
    if len(list) % 2 == 1:
        list = list + ["BYE"]

    for i in range(len(list)-1):

        mid = int(len(list) / 2)
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()	

        s = s + [ tuple(zip(l1, l2)) ]

        # Rotate items in the list counter clock wise:
        list.insert(1, list.pop())

    return s


def generate_players(num_of_players):
    players_list = []
    for i in range(num_of_players):
        players_list.append(
            {
                "name": "p" + str(i + 1),
                "rank": randint(1500, 2000),
                "points": 0
            }
        )
    return players_list


players = generate_players(4)

for p in players:
    print(p["name"])

schedule = create_schedule(players)


for r in range(len(schedule)):
    for m in range(len(schedule[r])):
        print(f"{schedule[r][m][0]} VS {schedule[r][m][1]}")
        

# print(schedule[0][0])






