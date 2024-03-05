from time import sleep
from random import randint
import json

class Spaceship:
    def __init__(self, name, health, fuel, score):
        self.name = name
        self.fuel = health
        self.health = fuel
        self.score = score

    def __str__(self):
        return f"Spaceship {self.name} has {self.fuel} fuel and {self.health} health left"
    
    def save_progress(self):
        data_to_save = {
            "name": self.name,
            "health": self.health,
            "fuel": self.fuel,
            "score": self.score
        }
        # Serializing json
        json_object = json.dumps(data_to_save, indent=4)
        
        # Writing to sample.json
        with open("./data/progress.json", "w") as outfile:
            print("saving progress")
            outfile.write(json_object)
        
    def load_saved_progress():
        try:
            # Load events data from events.json file
            with open('./data/progress.json', 'r') as openfile:
                # Reading from json file
                print("Loading user saved progess from progress.json.....")
                saved_progress = json.load(openfile)
                print("Done laoading  saved progress:")
                loaded_spaceship = Spaceship(saved_progress["name"], saved_progress["health"], saved_progress["fuel"], saved_progress["score"])
                print(loaded_spaceship)

                return loaded_spaceship
        except FileNotFoundError:
            print("No progress file found, let's create one")
            return None

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