class Road:
    def __init__(self, name, hardness, mental_effect, wheel_dmg_effect):
        self.name = name
        self.hardness = hardness
        self.mental_effect = mental_effect
        self.wheel_dmg_effect = wheel_dmg_effect
    
    def get_hardness_factor(self):
        return self.hardness
    
    def get_name(self):
        return self.name