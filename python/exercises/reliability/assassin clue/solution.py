from utils import helper


def main():
    try:
        places_list: list = helper.get_plugin("./plugins/places.json")
    except:
        print("No places list was provided, the default will be used")
        places_list = []

    try:
        weapons_list: list = helper.get_plugin("./weapons.json")
    except:
        print("No places list was provided, the default will be used")


    
    
    pass

if __name__ == "__main__":
    main()