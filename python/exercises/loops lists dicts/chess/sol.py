from random import randint
import random

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

        # Rotate items in the list counter-clock-wise:
        list.insert(1, list.pop())

    return s


def generate_players(num_of_players):
    players_list = []
    for i in range(num_of_players):
        rank = randint(1500, 2000)
        players_list.append(
            {
                "name": "p" + str(i + 1),
                "initial_rank": rank,
                "rank": rank,
                "points": 0
            }
        )
    return players_list

def print_leaderboard(players, score_system):
    if score_system == "elo rank change":
        print(f"\n--- {score_system} LEADERBOARD ---")
        sorted_players = sorted(players, key= lambda d: (d["rank"] - d["initial_rank"]), reverse=True)
        for player in sorted_players:
            print(f"{player['name']} : {player['rank'] - player['initial_rank']}")
        print("------------------------")
    else:
        print(f"\n--- {score_system} LEADERBOARD ---")
        sorted_players = sorted(players, key= lambda d: d[score_system], reverse=True)
        for player in sorted_players:
            print(f"{player['name']} : {player[score_system]}")
        print("------------------------")

def battle(p1, p2):
    rev_elo_ratio = 1 - p1["rank"]/p2["rank"]
    p2_chances = 0.4 + rev_elo_ratio
    p1_chances = 0.4 - rev_elo_ratio
    draw_chances = 0.2

    # Let's say 0: draw, 1: p1 win, 2: p2 win
    result_list = [0, 1, 2]
    # choose based on the probabilities:
    return random.choices(result_list, weights=(draw_chances, p1_chances, p2_chances), k=1)


def predict_scores(p1, p2):
    exp_score_p1 = 1 / (1 + pow(10, ((p2["rank"] - p1["rank"])/400)))
    exp_score_p2 = 1 / (1 + pow(10, ((p1["rank"] - p2["rank"])/400)))
    return exp_score_p1, exp_score_p2


def simulate_tournament(schedule):
    print("\n***TOURNAMET STARTED!***")
    for r in range(len(schedule)):
        for m in range(len(schedule[r])):
            first_player = schedule[r][m][0]
            second_player = schedule[r][m][1]

            print(f"{first_player['name']} VS {second_player['name']}")

            first_player_expected_score, second_player_expected_score = predict_scores(first_player, second_player)
            battle_result = battle(first_player, second_player)[0]

            if battle_result == 0:
                # draw
                print(f"Draw!. Adding +0.5 points to both {first_player['name']} and {second_player['name']}")
                first_player["points"] += 0.5
                second_player["points"] += 0.5
                first_player["rank"] = round(first_player["rank"] + 32 * (0.5 - first_player_expected_score))
                second_player["rank"] = round(second_player["rank"] + 32 * (0.5 - second_player_expected_score))
            elif battle_result == 1:
                # player 1 won
                print(f"{first_player['name']} won. Adding +1 point")
                first_player["points"] += 1
                first_player["rank"] = round(first_player["rank"] + 32 * (1 - first_player_expected_score))
                second_player["rank"] = round(second_player["rank"] + 32 * (0 - second_player_expected_score))
            elif battle_result == 2:
                # player 2 won
                print(f"{second_player['name']} won. Adding +1 point")
                second_player["points"] += 1
                second_player["rank"] = round(second_player["rank"] + 32 * (1 - second_player_expected_score))
                first_player["rank"] = round(first_player["rank"] + 32 * (0 - first_player_expected_score))
            else:
                # Error
                print("Error")
    print("\n***TOURNAMET FINISHED***")

##--------------------------------------------------------
##--------------------------------------------------------

players = generate_players(4)

print_leaderboard(players, 'rank')

schedule = create_schedule(players)

simulate_tournament(schedule)

print_leaderboard(players, 'points')
print_leaderboard(players, 'rank')
print_leaderboard(players, 'elo rank change')







