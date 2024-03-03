class Numbers:
    def __init__(self):
        self.result = True
        self.val_to_test = None

    def __str__(self):
        return str(self.result)

    def test(self, val_to_test):
        self.result = True # Initialize
        self.val_to_test = val_to_test
        return self

    def is_equal(self, num):
        self.result = self.result and (self.val_to_test == num)
        return self

    def is_greater_than(self, num):
        self.result = self.result and (self.val_to_test > num)
        return self

    def is_less_than(self, num):
        self.result = self.result and (self.val_to_test < num)
        return self


if __name__ == "__main__":
    print("You are running code directly")
else:
    print("Imported Testing Module!")