# Packing game

class Item:
    def __init__(self, name, weight, category):
        self.name = name.lower()
        self.weight = weight
        self.category = category
        self.allowed_categories = ["misc", "electronics", "sport"]
        if category not in self.allowed_categories:
            raise Exception(f"Chosen category: {self.category} is not allowed")

        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("Name should be a non empty string")
        if not isinstance(self.weight, (int, float)):
            raise Exception("Weight should be a number")
        if weight <= 0:
            raise Exception("Weight should be a positive non zero value")

    def get_weight(self):
        return self.weight
    
    def __str__(self):
        return self.name

class Product(Item):
    def __init__(self, name, weight, category, other_categories = [], other_details = {}):
        super().__init__(name, weight, category)
        self.other_categories = other_categories
        self.other_details = other_details
    
    def __str__(self):
        return self.name
    
    def get_details(self):
        details_string = ""
        if len(self.other_categories):
            for cat in self.other_categories:
                details_string += " " + str(cat)
                
        return f"{self.name} {self.weight} grams" + details_string


class Colored:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return str(self.color)

class Branded:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return self.brand

class Sized:
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return str(self.size)

class Priced:
    def __init__(self, price):
        self.price = price
    def __str__(self):
        return str(self.price)

class Origined:
    def __init__(self, origin):
        self.origin = origin
    def __str__(self):
        return self.origin

class Materialed:
    def __init__(self, material):
        self.material = material
    def __str__(self):
        return self.material

class With_camera:
    def __init__(self, camera_specs):
        self.camera_specs = camera_specs
    def __str__(self):
        return self.camera_specs

class Bag:
    def __init__(self, weight_limit, count_limit = 1):
        self.weight_limit = weight_limit
        self.count_limit = count_limit
        self.current_weight = 0
        self.all_items: list[Product] = []

    def add_item(self, product: Product, amount):
        new_weight = self.current_weight + (product.get_weight() * amount)
        new_count = len(self.all_items) + amount
        if new_weight <= self.weight_limit:
            if new_count <= self.count_limit:
                self.all_items.extend([product] * amount)
                self.current_weight = new_weight
                print(f"Added: {product} - updated: bag weight: {self.current_weight}/{self.weight_limit}, it now has {len(self.all_items)}/{self.count_limit} items inside it")
            else:
                print(f"Can't add item ({product}), Count limit exceeded: {new_count}/{self.count_limit}.")

        else:
            print(f"Can't add item ({product}), weight limit exceeded: {new_weight}/{self.weight_limit}")
    
    def get_all(self):
        for item in self.all_items:
            yield item
    
    def get_all_by_cat(self, category):
        for item in self.all_items:
            if category in item.category:
                yield item
        pass



my_bag = Bag(80, 6)
my_bag.add_item(Product("universal charger", 12, "electronics", [Colored("black"), Priced(50), Sized("M"), Branded("Lenovo")]), 1)
my_bag.add_item(Product("passport", 1, "misc", [Colored("blue"), Priced(50), Origined("USA")]), 1)
my_bag.add_item(Product("sunglasses", 10, "sport", [Colored("black")]), 1)
my_bag.add_item(Product("sneakers", 14, "sport", [Branded("new balance"), Origined("Spain")]), 1)
my_bag.add_item(Product("smart phone", 12, "electronics", [Branded("Apple"), Materialed("lithium, plastic")], {"OS": "iOS", "storage": "128 GB", "display": "AMOLED"}), 1)
my_bag.add_item(Product("laptop", 1, "electronics", [Branded("DELL")], {"Processor": "intel i7", "ram": "16 GB", "storage": "512 GB SSD", "Graphics": "NVIDIA GeForce4"}), 1)
my_bag.add_item(Product("smart watch", 44, "electronics", [Branded("Samsung")], {"Display": "Touchscreen", " Battery Life": "3 days", " Fitness Features": "Heart Rate Monitor", "Connectivity": "Bluetooth"}), 1)
my_bag.add_item(Product("campus", 4, "electronics", [Branded("Samsung"), Priced(50), Materialed(" iron, plastic")], {"accuracy": "high", " Battery Life": "3 days", " Fitness Features": "Heart Rate Monitor", "Connectivity": "Bluetooth"}), 1)

print("\n")
print("All items in the bag:")
for prod in my_bag.get_all():
    print(prod.name)

print("\n")
print("All items by category:")
for i in my_bag.get_all_by_cat("misc"):
    print(i)