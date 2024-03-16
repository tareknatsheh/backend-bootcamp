# Truck Simulator (Extendability)

This is a truck driving sumulator.
The user picks a truck type and provides a terrain as a json file.
The simulator simulates driving the truck on each and every road in the provided terrain.

## Quick start
#### 1. install the requirments
`pip install -r requirements.txt`

#### 2. make sure to have a terrain file (example: my_terrain.json)
#### 3. run the code
`python solution.py`


## Adding a plugin
You can add a truck or a road plugin by adding a new file to `plugins/trucks` or `plugins/roads`

Example of truck plugin:
```python
from .Main import Truck

# Truck(max_fuel_amount, km_per_liter, cost_wheels_per_km, brand)
truck = Truck(300, 6.5, 3, "Ford F-150")
```

**Every plugin class MUST have certain methods and parameters:**
### **truck plugin**
#### The constants:
* max fuel amount
* km per liter
* price to repair wheels per km
* brand
#### The variables:
- fuel (decreases after driving some km)
- wheels fix rate (affected by the road conditions - takes a factor from the road)

### **road plugin**
#### constants:
* name
* terrain hardness
* mental effect
* wheel damage effect

### **driver class**
#### constants:
- name
- age
- gender
variables:
- mental health (afcted by: road "mental effect" and km driven)