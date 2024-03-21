"""
Clue Assassin usin TDD

Basic components:
Player class:
    parameters:
        name, is_murderer, list of visited places, list of fav weapons
    methods:
        randomly show 2 visited places and 1 fav weapon
            return example [["p1", "p2"], ["w1"]]

Basic actions:
1) accuse:
    parameters:
        - player
    returns:
        - True or False (aka. if the accusation was true or false)

2) suspect:
    parameters:
        - player
    returns:
        - list of some of visited places and another list of some fav weapons

3) kill:
    parameters:
        - list of all alive players
    returns:
        - new list of alive players (will be missing the victim)


"""

import time
import random

from components.Player import *
from utils import helpers as h, printers as p


def main():

    import_places()

    # -- Pre-round configurations --
    # Create 4 players
    players = random_players_creator(4, Player)
    
    active  = True
    while active:
        # Start the game:
        p.print_welcome()
        time.sleep(1)

        # Reset all players (make them all alive and innocents)
        reset(players)
        # Define the killer
        killer = set_random_murderer(players)

        # At the beggining all players at alive
        alive_players = players

        # they can suspect only 2 players at each round, so keep a suspect counter.
        # And they can accuse once, then the round finishes
        session_is_active = True
        suspect_counter = 0
        rounds_counter = 0
        while session_is_active:
            # -- Start! --
            # If there is only one player left, then they are the killer, and you lost
            if len(alive_players) == 2 and suspect_counter == 0:
                session_is_active = False
                p.print_game_over()
                active = h.do_you_want_to_play_again()
            else:
                # When the suspect counter is 0 we know for sure that it is the start of the round
                # So, let's now define murder weapon, place and the victim
                if suspect_counter == 0:
                    rounds_counter += 1
                    print(f"\n---- Round {rounds_counter} ----")
                    # Define the place of murder and the weapon
                    murder_place = get_a_random_place_from_player(killer)
                    murder_weapon = random.choice(killer.list_fav_weapons)

                    # Kill the a victim randomly
                    kill_random_player(alive_players, killer)

                    print(f"Place of the murder: {murder_place}\nWeapon found in crime scene: {murder_weapon}")
                    time.sleep(2)

                    # Put the alive players in a list
                    alive_players = filter_alive_players(players)

                    # Show alive players to the user:
                    p.list_names(alive_players)

                # give the option to choose one to 'suspect' or 'accuse' and handle the choice
                if suspect_counter < 2:
                    print("\nDo you want to suspect or accuse any of them?")
                    user_choice = input(f"1) Investigate a Suspect ({suspect_counter}/2)\n2) Accuse!\n")
                    if user_choice == "1":
                        suspect_counter += 1
                        chosen_sus_num = int(input(f"Who do you suspect? (enter the number of the player between 1 - {len(alive_players)})\n"))
                        h.investigate_suspect(chosen_sus_num, alive_players)
                        
                    elif user_choice == "2":
                        # Accuse!
                        # And it's the last thing you can do in a round, so it's the end of the round:
                        # Handle the accusation, and decide to end the game or to continue
                        suspect_counter = 0
                        is_accusation_correct, accused_player = h.accuse(alive_players)
                        if is_accusation_correct:
                            session_is_active = False
                            p.print_congrats()
                            print("session is active: ", session_is_active)
                            active = h.do_you_want_to_play_again()
                        else:
                            print(f"-- Wrong accusation! {accused_player.name} is innocent --")
                    else:
                        raise Exception("wrong choice")
                else:
                    suspect_counter = 0
                    user_choice = input(f"Would you like now to accuse someone? (y/n)\n").lower()
                    if user_choice == "y":
                        # Handle the accusation, and decide to end the game or to continue
                        is_accusation_correct, accused_player = h.accuse(alive_players)
                        if is_accusation_correct:
                            session_is_active = False
                            p.print_congrats()
                            active = h.do_you_want_to_play_again()
                        else:
                            print(f"Wrong accusation! {accused_player.name}")
                    else:
                        print("-- No player was accused, let's start the next round --")

        # If accuse: if player is the killer --> you win! finish the game and ask if user wants to play again
        # If accuse: if player is innocent --> the round is immediatly finishes and the next one starts


        # active  = False
    print("Bye bye")
    pass

if __name__ == "__main__":
    main()