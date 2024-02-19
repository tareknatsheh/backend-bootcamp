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


p1 = Pokemon("pikachu1", 8, 3, "earth")
p2 = Pokemon("Bulbasaur1", 3, 2, "earth")
p3 = Pokemon("Squirtle1", 6, 2, "water")
p4 = Pokemon("Charmander1", 9, 1, "fire")
p5 = Pokemon("Pidgey1", 2, 5, "wind")

p6 = Pokemon("pikachu2", 8, 3, "earth")
p7 = Pokemon("Bulbasaur2", 3, 2, "earth")
p8 = Pokemon("Squirtle2", 6, 2, "water")
p9 = Pokemon("Charmander2", 9, 1, "fire")
p10 = Pokemon("Pidgey2", 2, 5, "wind")

person1 = [p1, p2, p3, p4, p5]
person2 = [p6, p7, p8, p9, p10]

random.shuffle(person1)
random.shuffle(person2)

# Select first opponents:
first_pok = person1.pop()
second_pok = person2.pop()

while (first_pok) and (second_pok):
    attacker_index = who_will_attack_first(first_pok.speed, second_pok.speed)
    if attacker_index:
        is_p1_attacker = False
        attack_pok = second_pok
        defend_pok = first_pok
        attack_person = person2
        defend_person = person1
    else:
        is_p1_attacker = True
        attack_pok = first_pok
        defend_pok = second_pok
        attack_person = person1
        defend_person = person2
    
    damage = type_modifier(attack_pok.type, defend_pok.type) * (random.randint(1, 20) + attack_pok.strength)
    defend_pok.life -= damage
    print(f"{attack_pok.name} attacks {defend_pok.name}. deals {damage} damage. {defend_pok.name} now has {defend_pok.life} amount of life after the attack.")
    if defend_pok.life <= 0:
        print(f"{defend_pok.name} is dead!")
        if is_p1_attacker:
            if len(person2) <= 0:
                second_pok = None
                break
            second_pok = person2.pop()
            print(f"{second_pok.name} has joind the fight!")
        else:
            if len(person1) <= 0:
                first_pok = None
                break
            first_pok = person1.pop()
            print(f"{first_pok.name} has joind the fight!")


if second_pok:
    print("Second person is the winner!")
else:
    print("First person is the winner!")
        

