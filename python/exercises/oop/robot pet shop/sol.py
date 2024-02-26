# Robot Pet Shop

# We have the following entities:
# Shop: it has: employees, robot pets for sale, robot pets in repair and a balance
# Robot: has: name, id, battery type and one status (for sale, broken, in repair, prepared to be
#   shipped or sold)
# Employees: they happen to be robots, so they have:
#   everything in robot + a daily salary
# Robot pets: they have:
#   everything in robot +  main material, price, cost_to_fix_per_day and animal type


class Shop:
    def __init__(self):
        self.__employees = []
        self.__robot_pets = []
        self.__balance = 1000
    
    def add_employee(self, employee):
        self.__employees.append(employee)

    def add_robot_pet(self, robot_pet):
        self.__robot_pets.append(robot_pet)

    def __find_robot_pet(self, id = None, name = None):
        if id == None and name == None:
            raise Exception("Please provide and id or a name")
        else:
            for index, pet in enumerate(self.__robot_pets):
                if pet.id == id or pet.name == name:
                    return index, pet
            # Couldn't find the pet in the shop:
            raise Exception(f"Can't find robot with id {id} in the store")

    def get_balance(self):
        return self.__balance

    def sell(self, robot_pet_id):
        wanted_pet_index, wanted_pet_obj = self.__find_robot_pet(robot_pet_id)
        wanted_pet_obj._change_status("sold")
        self.__balance += wanted_pet_obj.price
        self.__robot_pets.pop(wanted_pet_index)
        print(f"Sold: {wanted_pet_obj.name} with price {wanted_pet_obj.price}")
        return wanted_pet_obj
    
    def get_all_with_status(self, status):
        for pet in self.__robot_pets:
            if pet.status == status:
                yield pet
    
    def get_for_sale_with_price_range(self, lower_price, higher_price):
        for pet in self.get_all_with_status("for sale"):
            if pet.price >= lower_price and pet.price <= higher_price:
                yield pet

    def get_employees_total_cost_per_day(self):
        total = 0
        for employee in self.__employees:
            total += employee.daily_salary
        
        return total
    
    def get_robot_pet_details(self, id = None, name = None):
        wanted_pet_index, wanted_pet_obj = self.__find_robot_pet(id, name)
        details = ""
        for attr in dir(wanted_pet_obj):
            # Getting rid of dunder methods
            if not attr.startswith("_"):
                details += attr + ": " + str(getattr(wanted_pet_obj, attr)) + "\n"
        return details
                    
            
            
class Robot:
    def __init__(self, name, id, battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type
        if battery_type not in ["lithium", "alkaline"]:
            raise Exception(f"Wrong battery type: {battery_type}")


class Employee(Robot):
    def __init__(self, name, id, battery_type, daily_salary):
        super().__init__(name, id, battery_type)
        self.daily_salary = daily_salary


class Robot_pet(Robot):
    def __init__(self, name, id, battery_type, main_material, price, cost_to_fix_per_day, animal_type, status):
        super().__init__(name, id, battery_type)
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.animal_type = animal_type
        self._change_status(status)

        if animal_type not in ["herbivore", "carnivore"]:
            raise Exception(f"Wrong animal type: {animal_type}")


    def _change_status(self, new_status):
        if new_status not in ["for sale", "broken", "in repair", "to be shipped", "sold"]:
            raise Exception(f"Wrong status value: {new_status}")
        else:
            self.status = new_status
    

##------------------------------------------------------------------
##------------------------------------------------------------------

our_shop = Shop()
print("Shop starting balance: ", our_shop.get_balance())

emp1 = Employee("emp1", 1, "lithium", 150)
emp2 = Employee("emp2", 2, "lithium", 160)

our_shop.add_employee(emp1)
our_shop.add_employee(emp2)

pet1 = Robot_pet("pet1", 1, "lithium", "ss", 35, 5, "carnivore", "broken")
pet2 = Robot_pet("pet2", 2, "alkaline", "plastic", 50, 2, "herbivore", "for sale")
pet3 = Robot_pet("pet3", 3, "alkaline", "rubber", 60, 20, "carnivore", "for sale")
pet4 = Robot_pet("pet4", 4, "lithium", "ss", 43, 10, "herbivore", "in repair")
pet5 = Robot_pet("pet5", 5, "lithium", "ss", 15, 10, "herbivore", "for sale")

our_shop.add_robot_pet(pet1)
our_shop.add_robot_pet(pet2)
our_shop.add_robot_pet(pet3)
our_shop.add_robot_pet(pet4)
our_shop.add_robot_pet(pet5)

sold_pet = our_shop.sell(3)

# print all pets available for sale in the store
print("\nAvailable pets for sale:")
for pet in our_shop.get_all_with_status("for sale"):
    print(pet.name)

# print all robots in repair
print("\nRobots in repair:")
for pet in our_shop.get_all_with_status("in repair"):
    print(pet.name)

#  print all pets available for sale, based on price range
lower_price = 10
higher_price = 50
print("\nRobots for sale in defined price range:")
for pet in our_shop.get_for_sale_with_price_range(lower_price, higher_price):
    print(pet.name)

# print all employees salary cost
print(f"\nTotal daily salary cost: {our_shop.get_employees_total_cost_per_day()}")

# print store balance
print("\nTotal shop balance: ", our_shop.get_balance())

# print robot details based on id or name
pet_id_to_explore = 2
print(f"\nDetails of robot pet with id = {pet_id_to_explore} are:" )
print(our_shop.get_robot_pet_details(pet_id_to_explore))
