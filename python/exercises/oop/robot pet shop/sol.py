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

    def get_balance(self):
        return self.__balance

    def sell(self, robot_pet_id):
        for index, pet in enumerate(self.__robot_pets):
            if pet.id == robot_pet_id:
                print(f"Selling: {pet.name} id: {pet.id}")
                wanted_pet = self.__robot_pets.pop(index)
                wanted_pet.change_status("sold")
                self.__balance += wanted_pet.price
                return wanted_pet
        
        # Couldn't find the pet in the shop:
        raise Exception(f"Can't find robot with i{robot_pet_id} in the store")
    
    def get_all_available_pets_for_sale(self):
        for pet in self.__robot_pets:
            if pet.status == "for sale":
                yield pet


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
        self.change_status(status)

        if animal_type not in ["herbivore", "carnivore"]:
            raise Exception(f"Wrong animal type: {animal_type}")


    def change_status(self, new_status):
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

our_shop.add_robot_pet(pet1)
our_shop.add_robot_pet(pet2)
our_shop.add_robot_pet(pet3)


print("balance: ", our_shop.get_balance())

for item in our_shop.get_all_available_pets_for_sale():
    print(item.name)
