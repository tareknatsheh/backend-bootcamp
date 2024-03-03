class Lists:
    def __init__(self):
        self.result = True
        self.val_to_test = None
    
    def __str__(self):
        return str(self.result)

    def test(self, val_to_test):
        self.result = True # Initialize
        self.val_to_test = val_to_test
        return self
    
    def is_in_list(self, list = []):
        self.result = self.result and (self.val_to_test in list)
        return self