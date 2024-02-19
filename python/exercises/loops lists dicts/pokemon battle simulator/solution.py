import random

class Pokemon:
    def __init__(self, name, strength, speed, type):
        self.name = name
        self.level = 1
        self.strength = strength
        self.speed = speed
        self.type = type
        self.life = 120

def who_will_attack_first(first_pok_speed, second_pok_speed):
    first_pok_total_speed = random.randint(1, 20) + first_pok_speed
    second_pok_total_speed = random.randint(1, 20) + second_pok_speed

    if first_pok_total_speed > second_pok_total_speed:
        return 0
    else:
        return 1


types_matrix = {
    "fire": {
        "fire": 1,
        "water": 2,
        "earth": 1,
        "wind": 2
    },
    "water": {
        "fire": 2,
        "water": 1,
        "earth": 2,
        "wind": 1
    },
    "earth": {
        "fire": 2,
        "water": 1,
        "earth": 1,
        "wind": 2
    },
    "wind": {
        "fire": 1,
        "water": 2,
        "earth": 1,
        "wind": 1
    }
}
def type_modifier(attacker_type, defender_type):
    return types_matrix[attacker_type][defender_type]


p1 = Pokemon("pikachu", 8, 3, "earth")
p2 = Pokemon("Bulbasaur", 3, 2, "earth")
p3 = Pokemon("Squirtle", 6, 2, "water")
p4 = Pokemon("Charmander", 9, 1, "fire")
p5 = Pokemon("Pidgey", 2, 5, "wind")

p6 = Pokemon("pikachu", 8, 3, "earth")
p7 = Pokemon("Bulbasaur", 3, 2, "earth")
p8 = Pokemon("Squirtle", 6, 2, "water")
p9 = Pokemon("Charmander", 9, 1, "fire")
p10 = Pokemon("Pidgey", 2, 5, "wind")

person1 = [p1, p2, p3, p4, p5]
person2 = [p6, p7, p8, p9, p10]

random.shuffle(person1)
random.shuffle(person2)

# Select first opponents:
first_pok = person1.pop()
second_pok = person2.pop()

while (len(person1) > 0) and (len(person2) > 0):
    attacker_index = who_will_attack_first(first_pok.speed, second_pok.speed)
    if attacker_index:
        attacker = second_pok.name
        defender = first_pok.name
        damage = type_modifier(second_pok.type, first_pok.type) * (random.randint(1, 20) + second_pok.strength)
        first_pok.life -= damage
        defender_life = first_pok.life
        if first_pok.life <= 0:
            print(f"{first_pok.name} is dead!")
            first_pok = person1.pop()
            print(f"{first_pok.name} has joind the fight!")
    else:
        attacker = first_pok.name
        defender = second_pok.name
        damage = type_modifier(first_pok.type, second_pok.type) * (random.randint(1, 20) + first_pok.strength)
        second_pok.life -= damage
        defender_life = second_pok.life
        if second_pok.life <= 0:
            print(f"{second_pok.name} is dead!")
            second_pok = person2.pop()
            print(f"{second_pok.name} has joind the fight!")
    
    print(f"{attacker} attacks {defender}. deals {damage} damage. {defender} now has {defender_life} amount of life after the attack.")


if len(person1) <= 0:
    print("Second person is the winner!")
else:
    print("First person is the winner!")
        
print(f"person1 has {len(person1)} pokemons left")
print(f"person2 has {len(person2)} pokemons left")