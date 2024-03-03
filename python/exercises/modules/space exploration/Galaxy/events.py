from random import choices

possible_events = [
    {
        "name": "Asteroid Field",
        "probability": 0.3,
        "actions": [
            {
                "name": "fire",
                "health_cost_range": [-40, -20],
                "fuel_cost_range": [-10, -5]
            },
            {
                "name": "evade",
                "health_cost_range": [-10, 0],
                "fuel_cost_range": [-50, -30]
            }
        ]
    },
    {
        "name": "Alien Diplomacy",
        "probability": 0.4,
        "actions": [
            {
                "name": "accept",
                "health_cost_range": [20, 60],
                "fuel_cost_range": [-20, -10]
            },
            {
                "name": "refuse",
                "health_cost_range": [0, 0],
                "fuel_cost_range": [0, 0]
            }
        ]
    },
    {
        "name": "Space Pirates",
        "probability": 0.4,
        "actions": [
            {
                "name": "fight",
                "health_cost_range": [-60, -10],
                "fuel_cost_range": [-10, -5]
            },
            {
                "name": "run away",
                "health_cost_range": [-10, 0],
                "fuel_cost_range": [-50, -30]
            }
        ]
    },
    {
        "name": "Black Hole",
        "probability": 0.1,
        "actions": [
            {
                "name": "get into it",
                "health_cost_range": [-60, 90],
                "fuel_cost_range": [-20, 90]
            },
            {
                "name": "run away",
                "health_cost_range": [0, 0],
                "fuel_cost_range": [-30, -20]
            }
        ]
    },
    {
        "name": "Free resources",
        "probability": 0.3,
        "actions": [
            {
                "name": "get it",
                "health_cost_range": [5, 20],
                "fuel_cost_range": [10, 30]
            },
            {
                "name": "ignore it",
                "health_cost_range": [0, 0],
                "fuel_cost_range": [0, 0]
            }
        ]
    }
]
wights_of_each = [x["probability"] for x in possible_events]

def get_event():
    return choices(possible_events, weights=wights_of_each, k=1)[0]
