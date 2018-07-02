# CLASSES
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):  # String representation
        return "The {} menu is served between {} & {}.".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):  # String representation
        return "The address of this restaurant is {}".format(self.address)

    def available_menus(self, time):
        avail = [menu for menu in self.menus if time >= menu.start_time and time <= menu.end_time]
        return avail


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):  # String representation
        return "Business Name: {} with {} location/s nationwide".format(self.name, len(self.franchises))


# MENU OBJECTS
brunch = Menu("brunch",
              {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
               'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)

dinner = Menu("dinner",
              {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
               'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

arepas = Menu("arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},
              1000, 2000)

# FRANCHISE OBJECTS
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas])

# BUSINESS OBJECTS
pasta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa_business = Business("Take a' Arepa", [arepas_place])

# TEST PRINTS
# Testing menus
print(brunch, early_bird, dinner, kids)
print(arepas)
print()

# Testing .calculate_bill method
print("Your Brunch Bill: $", brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(["pancakes", "home fries", "coffee"])
print("Your Early Bird Bill: $", early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))
print(["salumeria plate", "mushroom ravioli (vegan)"])
print("Your Arepas Bill: $", arepas.calculate_bill(["pernil arepa", "jamon arepa"]))
print(["pernil arepa", "jamon arepa"])
print()

# Testing Franchise
print(flagship_store)  # The address of this restaurant is 1232 West End Road
print(flagship_store.available_menus(1200))  # Available menus at this time
print(arepas_place)  # The address of this restaurant is 189 Fitzgerald Avenue
print(arepas_place.available_menus(1400))  # Available menus at this time
print()

# Testing Businesses
print(pasta_business)
print(arepa_business)
print()
