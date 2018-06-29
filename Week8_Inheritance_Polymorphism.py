# Parent Class, SubClass
class User:  # Parent Class
  is_admin = False
  def __init__(self, username):
    self.username = username
class Admin(User):  # SubClass, with (ParentClass) 
  is_admin = True


# Exception Class Example
  class OutOfStock(Exception):  # Exception Class defined like this
    pass
# Updated the class below to raise OutOfStock Exception
  class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"
    def __init__(self, stock):
      self.stock = stock
    def buy(self, color):
      if self.stock[color] == 0:
        raise OutOfStock
      else:
        self.stock[color] = self.stock[color] - 1
  candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
  candle_shop.buy('blue')
  candle_shop.buy('green')  # This should raise OutOfStock:


# Example of an Overriding Method
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
class User:
    def __init__(self, username):
        self.username = username
    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text
# Admin(User) subclass is redefining  edit_message (which is under edit_message) and just assumes no if statement needed
class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text


# Example of Super() where you initialize a subclass like a parent
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions
class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40


# Example of Interfaces, where we dont care what class an object belongs to, just whether the class can perform the task
# needed for the object.
class InsurancePolicy:  # Parent Class
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item
class VehicleInsurance(InsurancePolicy):  # Subclass
    def get_rate(self):  # Same method as below
        return self.price_of_insured_item * .001
class HomeInsurance(InsurancePolicy):  # Subclass
    def get_rate(self):  # Same method as above
        return self.price_of_insured_item * .00005


# Example of Polymorphism, is a term used to describe the same syntax (like + operator) doing different actions
# depending on the data type.
2 + 4 == 6  # For an int and an int, + returns an int
3.1 + 2.1 == 5.2  # For a float and a float, + returns a float
"Is this " + "addition?" == "Is this addition?"  # For a string and a string, + returns a string
[1, 2] + [3, 4] == [1, 2, 3, 4]  # For a list and a list, + returns a list
# Another example would be the "len" method used in different ways but produces the same response, flexible
a_list = [1, 18, 32, 12]
print(len(a_list))  # Prints 4
a_dict = {'value': True}
print(len(a_dict))  # Prints 1
a_string = "Polymorphism is cool!"
print(len(a_string))  # Prints 21


# Example of Dunder Methods:
# Give Atom a .__add__(self, other) method that returns a Molecule with the two Atoms.
class Atom:
    def __init__(self, label):
        self.label = label
    def __add__(self, other):  # Dunder Method
        return Molecule([self, other])
class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine


# Example of Dunder Method:
# Give LawFirm a .__len__() method that will return the number of lawyers in the law firm.
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers
    def __len__(self):
        return len(self.lawyers)
    def __contains__(self, lawyer):
        return lawyer in self.lawyers
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])


# Review Exercise:
# Create a class SortedList that inherits from the built-in type list.
# Recall that lists have a .append() method that takes a two arguments, self and value. We're going to have SortedList perform a sort after every .append().
# First, we want our new .append() to actually add the item to the list. Write the code that would get SortedList to behave like a normal list when calling the .append() method.
# After you've appended the new value, sort the list.
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
