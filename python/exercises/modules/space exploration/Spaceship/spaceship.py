from time import sleep

class Spaceship:
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health
    
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

    def explore(self):
        pass

    def handle_event(self, event = {}):
        print("\nAttention! we got:")
        print(event["name"])
        # print("prob for this event is: ", event["probability"])
        print("What to do??")
        for index, choice in enumerate(event["actions"]):
            print(f"{index + 1})", choice["name"])
        user_choice = input("\n")
        if user_choice.lower() == "q":
            print("Going back to base...")
            sleep(1)
            return True
        
        print(event["actions"][int(user_choice) - 1])