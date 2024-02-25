from random import sample, randint
### its ok to use placeholders at start, not at the end. this is not what is reuqired in the exe
materials = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't'
]

class Delegation:
    def __init__(self, name, needed_material, num_of_suggestions):
        self.name = name
        self.needed_material = needed_material 
        self.num_of_suggestions = num_of_suggestions
        self.is_open_for_negotiation = True

    def is_offer_accepted(self, offered_material):
        if self.is_open_for_negotiation:
            # Check if the offered material is needed
            # if so --> return true, otherwise --> return false
            if offered_material in self.needed_material:
                return True
            else:
                self.num_of_suggestions -= 1
                if self.num_of_suggestions <= 0:
                    self.is_open_for_negotiation = False


# Set the range of acceptable number of suggestions (min - max) for the dummy examples:
num_of_suggestions_a = 5
num_of_suggestions_b = 10

### DRY 
### also from clean code point of view - do you understand what is happening when you create a delegation?
alien_delegation1 = Delegation("alien1", sample(materials,randint(2, 3)), randint(num_of_suggestions_a, num_of_suggestions_b))
alien_delegation2 = Delegation("alien2", sample(materials,randint(2, 3)), randint(num_of_suggestions_a, num_of_suggestions_b))
alien_delegation3 = Delegation("alien3", sample(materials,randint(2, 3)), randint(num_of_suggestions_a, num_of_suggestions_b))
alien_delegation4 = Delegation("alien4", sample(materials,randint(2, 3)), randint(num_of_suggestions_a, num_of_suggestions_b))

### what if it was 500 aliend delegations?
### try to make it dynamic
alien_delegation_list = [alien_delegation1, alien_delegation2, alien_delegation3, alien_delegation4]

convinced_aliens_couter = 0
num_failed_attempts = 0

for alien in alien_delegation_list:
    print(alien.name)
    print(alien.num_of_suggestions)
    # Let's take a random unique list of suggestions for this alien equals to # of allowed suggestions by this alien:
    offer_sample_size = len(materials) if alien.num_of_suggestions > len(materials) else alien.num_of_suggestions
    ### why generate the offered list here and not when generating the delegation?
    offered_materials_list = sample(materials, offer_sample_size)

    for offered_item in offered_materials_list:
        if alien.is_offer_accepted(offered_item):
            print(f"Great! {alien.name} is with us")
            convinced_aliens_couter += 1
            break
        else:
            num_failed_attempts += 1

    print(f"Total # of convinced aliens: {convinced_aliens_couter}")
    print(f"Total # of failed attempts: {num_failed_attempts}")
