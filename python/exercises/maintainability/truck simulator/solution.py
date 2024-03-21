"""
Truck Simulator (Extendability)

TODO:
add more comments and docstring
create block diagram and add it to Readme.md
"""

import plugins.trucks_plugins_manager as tr
import plugins.roads_plugins_manager as rd
from utils.simulator import simulate

def can_truck_do_this_terrain(truck_module, terrain_obj):
    return tr.get_full_tank_km(truck_module) >= rd.get_total_km(terrain_obj)

def main():
    print("---- Weclome to the ultimate Truck Simulator ----")

    active: bool = True
    while active:
        # Ask user to choose truck:
        print("Please choose a truck type:")
        for index, option in enumerate(tr.get_names_all_available_trucks()):
            print(f"{index}) {option}")
        chosen_truck = int(input(""))
        my_truck = tr.get_truck(chosen_truck)
        print(f"You have chosen {my_truck.get_name()}")

        # Ask user to specify the path to the terrain file:
        chosen_terrain = rd.get_terrain_file()

        # Check if the chosen truck can do the terrain on a full tank:
        can_do_it: bool = can_truck_do_this_terrain(my_truck, chosen_terrain)

        print(f"Can our truck do it? {can_do_it}")

        if can_do_it:
            # Let's proceed
            print("-"*10)
            print("- Here we go!-")
            print("-"*10)
            simulate(my_truck, chosen_terrain, {})
            
            do_try_again = input("\nWould you like to try again? (y/n)\n").lower()
            active = True if do_try_again == "y" else False
            # print_truck_state(new_truck_state)
            # print_driver_state(driver_mental_state)
        else:
            print("This truck can't do this terrain!")
        
        # active = print_try_again()

    
    print("Bye bye!")


    pass

if __name__ == "__main__":
    main()