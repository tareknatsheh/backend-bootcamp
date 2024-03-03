import json
from random import choices

# Load events data from events.json file
with open('./data/events.json', 'r') as openfile:
    # Reading from json file
    print("Loading events from events.json.....")
    possible_events = json.load(openfile)
    print("Done laoading  events")

wights_of_each = [x["probability"] for x in possible_events]

# To seed some initial values to our events.json, uncommeent this and provide a dict with the data
# def seed(dictionary):
#     # Serializing json
#     json_object = json.dumps(dictionary, indent=4)
    
#     # Writing to sample.json
#     with open("../data/events.json", "w") as outfile:
#         outfile.write(json_object)
# seed(data)

def get_event():
    return choices(possible_events, weights=wights_of_each, k=1)[0]


