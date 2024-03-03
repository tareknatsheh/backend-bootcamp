# Space exploration

# Structure of the game will be as the following:
# I'll keep taking users's input to decide what to do
# Start with asking the user to launch the ship (aka start the game)
# Then after some delay show a random event
# Ask the user to respons by giving them options relevant to the event
# Now we have an event and a corresponding responce from the user!
# We then calculate health and fuel based on the event and the response (?)
# If health or fuel is 0 --> user failed, ask them if they want to try again.

from Spaceship import ship
from Galaxy import events

my_ship = ship.Spaceship("spicy")

active = True
launched = False
while active:
    if not launched:
        print("\nWhat would you like to do")
        user_choice = input("1) Launch the Spaceship!\n2) View Spaceship details\n3) Exit\n")
        if user_choice == "1":
            # Start the game!
            my_ship.launch()
            launched = True
        elif user_choice == "2":
            # View spaceship details:
            print(my_ship)
            pass
        elif user_choice == "3":
            print("Exiting...")
            active = False
        else:
            print("Please enter 1, 2 or 3")
    else:
        an_event = events.get_event()
        quit = my_ship.handle_event(an_event)
        if quit:
            print("\n---- Main Menu ----")
            launched = False


