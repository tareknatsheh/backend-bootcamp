# Packing game

allowed_categories = ["misc", "electronics", "sport"]

class Item:
    def __init__(self, name, weight, category):
        self.name = name.lower()
        self.weight = weight
        self.category = category
        if category not in allowed_categories:
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

    def get_all_sort_by_cat(self):
        sorted_items_by_cat = sorted(self.all_items, key = lambda item: item.category)
        current_cat_to_print = ""
        for p in sorted_items_by_cat:
            # check if we enter a new category of items, if yes, print the category title:
            if current_cat_to_print != p.category:
                print('')
                print(p.category)
                current_cat_to_print = p.category
            print(p.name)
        pass



my_bag = Bag(80, 6)

appendix_a_list = [
    Product("universal charger", 12, "electronics", [Colored("black"), Priced(50), Sized("M"), Branded("Lenovo")]),
    Product("passport", 1, "misc", [Colored("blue"), Priced(50), Origined("USA")]),
    Product("sunglasses", 10, "sport", [Colored("black")]),
    Product("sneakers", 14, "sport", [Branded("new balance"), Origined("Spain")]),
    Product("smart phone", 12, "electronics", [Branded("Apple"), Materialed("lithium, plastic")], {"OS": "iOS", "storage": "128 GB", "display": "AMOLED"}),
    Product("laptop", 1, "electronics", [Branded("DELL")], {"Processor": "intel i7", "ram": "16 GB", "storage": "512 GB SSD", "Graphics": "NVIDIA GeForce4"}),
    Product("smart watch", 44, "electronics", [Branded("Samsung")], {"Display": "Touchscreen", " Battery Life": "3 days", " Fitness Features": "Heart Rate Monitor", "Connectivity": "Bluetooth"}),
    Product("campus", 4, "electronics", [Branded("Samsung"), Priced(50), Materialed(" iron, plastic")], {"accuracy": "high", " Battery Life": "3 days", " Fitness Features": "Heart Rate Monitor", "Connectivity": "Bluetooth"})
]

active = True
while active:
    user_choice = input("""\nWhat do you like to do?
1) Show all items in the bag
2) Show all items sorted by category
3) Print all items from a specific category
4) Add all items in 'APPENDIX A' to your bag
5) Add new item from products in Appendix A to your bag
6) Exit\n""")

    if user_choice == "1":
        print("\nAll items in the bag:\n")
        for prod in my_bag.get_all():
            print(prod.name)

    elif user_choice == "2":
        print("\nAll items by category:")
        my_bag.get_all_sort_by_cat()
    elif user_choice == "3":
        cat_choice = input(f"What category would you like to see?\n{allowed_categories}\n")
        print(f"\nPrint item only from category '{cat_choice}'")
        for item in my_bag.get_all_by_cat(cat_choice):
            print(item)
    elif user_choice == "4":
        for pdt in appendix_a_list:
            my_bag.add_item(pdt, 1)
    elif user_choice == "5":
        print("Here are all the products in Appendix A:")
        for item in appendix_a_list:
            print(item)
        print("Which one of them whould you like to add to your bag?")
        item_to_add_user_choice = input("Please enter the name of only one of them: ")
        found_item = list(filter(lambda c: c.name == item_to_add_user_choice, appendix_a_list))[0]
        if found_item:
            print("\nAdding...")
            my_bag.add_item(found_item, 1)
            print("")
    elif user_choice == "6":
        print("Exiting.....")
        active = False
    


