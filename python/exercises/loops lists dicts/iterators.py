class MyArray:
    def __init__(self, values):
        self.values = values
        self.current_index = 0
    
    def __iter__(self):
        return self


    def __next__(self):
        if self.current_index >= len(self.values):
            raise StopIteration
        
        value = self.values[self.current_index]
        self.current_index += 1

        return value
