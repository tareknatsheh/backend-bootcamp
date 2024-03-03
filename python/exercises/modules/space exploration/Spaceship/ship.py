from time import sleep
from random import randint

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.health = 100
        self.score = 0

    def __str__(self):
        return f"Spaceship {self.name} has {self.fuel} fuel and {self.health} health left"

    def launch(self):
        print("\nStarting the launch squence..")
        # sleep(1)
        # print("3")
        # sleep(1)
        # print("2")
        # sleep(1)
        print("1")
        sleep(1)
        print(f"Spaceship {self.name} is now in the sky!")
        print("Note: type 'Q' or 'q' to quit")

    def __update_health_and_fuel(self, health_points, fuel_points):
        self.health += health_points
        if self.health > 100: self.health = 100
        self.fuel += fuel_points
        if self.fuel > 100: self.fuel = 100
    

    def handle_event(self, event = {}):
        print("\nAttention! we got:")
        print(event["name"])
        # print("prob for this event is: ", event["probability"])
        print("What to do??")
        for index, choice in enumerate(event["actions"]):
            print(f"{index + 1})", choice["name"])
        print("q) Quit and go back to base")
        user_choice = input("\n")
        if user_choice.lower() == "q":
            print("Going back to base...")
            sleep(1)
            return True
        
        action_to_do = event["actions"][int(user_choice) - 1]
        health_effect_range = action_to_do["health_cost_range"]
        health_effect = randint(health_effect_range[0], health_effect_range[1])
        fuel_effect_range = action_to_do["fuel_cost_range"]
        fuel_effect = randint(fuel_effect_range[0], fuel_effect_range[1])

        print(f"Lets {action_to_do['name']}")
        print(f"You got {health_effect}% on health")
        print(f"You got {fuel_effect}% on fuel")
        
        sleep(2)
                
        self.__update_health_and_fuel(health_effect, fuel_effect)
        print(f"Health: {self.health} Fuel: {self.fuel}")
        
        if self.health <= 0:
            print("KAABOOOM! spacecraft turned into pieces")
            sleep(1)
            return True
        elif self.fuel <= 0:
            print("No fuel left, call the spacecraft trailer")
            sleep(1)
            return True
        else:
            # If user survived the event, give them some score
            self.score += 10