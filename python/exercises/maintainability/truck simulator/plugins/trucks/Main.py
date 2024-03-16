class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, cost_wheels_per_km, brand):
        self.max_fuel_amount = max_fuel_amount
        self.km_per_liter = km_per_liter
        self.cost_wheels_per_km = cost_wheels_per_km
        self.brand = brand
        self._current_fuel_level = max_fuel_amount
    
    def get_name(self):
        return self.brand

    def get_max_km(self):
        return self.km_per_liter * self.max_fuel_amount

    def get_km_per_liter(self):
        return self.km_per_liter

    def get_liter_per_km(self):
        return (1 / self.get_km_per_liter())

    def drive_km(self, km):
        self._current_fuel_level -= self.get_liter_per_km() * km

    def get_current_fuel_amount(self):
        return self._current_fuel_level