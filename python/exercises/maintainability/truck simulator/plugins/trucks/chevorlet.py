"""
A truck plugin
"""

# The constants:
_MAX_FUEL_AMOUNT = 200
_KM_PER_LITER = 8
_COST_WHEELS_PER_KM = 2
_BRAND = "2024 Chevrolet Silverado"

# The variables:
_current_fuel_level = _MAX_FUEL_AMOUNT

def get_name():
    return _BRAND

def get_max_km():
    return _KM_PER_LITER * _MAX_FUEL_AMOUNT

def get_km_per_liter():
    return _KM_PER_LITER

def get_liter_per_km():
    return (1 / get_km_per_liter())

def drive_km(km):
    global _current_fuel_level
    _current_fuel_level -= get_liter_per_km() * km

def get_current_fuel_amount():
    return _current_fuel_level