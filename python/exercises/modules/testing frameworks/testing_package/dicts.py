class Dicts:
    def __init__(self):
        self.result = True
        self.val_to_test = None
    
    def __str__(self):
        return str(self.result)

    def test(self, val_to_test):
        self.result = True # Initialize
        self.val_to_test = val_to_test
        return self
    
    def is_key_in_dict(self, dict = {}):
        self.result = self.result and (self.val_to_test in dict)
        return self

    def is_value_in_dict(self, dict = {}):
        self.result = self.result and (self.val_to_test in dict.values())
        return self