# CLASS = schematic for a data type
# OBJECT = instantiated instance of a class
# SELF = the self keyword refers to the object and not the class being called
# We can write our classes to structure the data that we need and write methods that will interact with that data.

# type() to figure out class type
print(type("String"))  # Prints <class "str">
print(type(5))  # Prints <class "int">
print(type(5.5))  # Prints <class "float">
my_dict = {}
print(type(my_dict))  # Prints <class "dict">
my_list = []
print(type(my_list))  # Prints <class "list">


# dir() can be used to find the available attributes of any object (ex. str, int, function, class, list, dict, etc)
print(dir(5))  # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
print(dir("String"))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
def this_function_is_an_object(list):
  return list
print(dir(this_function_is_an_object))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


# Defining a Class
class Facade:
    pass  # Use pass so we can leave the Class empty and not have an indentation error
facade_1 = Facade()  # We instantiate the class, by creating an object instance of it
facade_1_type = type(facade_1)  # We assign the "type" of the object we created to a new variable
print(facade_1_type)  # Prints <class "__main__.Facade">

# Examples of Accessing a Class's object outside the class, using object.variable
class Grade:
  minimum_passing = 65
# To access an class objects, use object.variable... so "Grade.minimum_passing"
print(Grade.minimum_passing)  # Prints the class variable "minimum_passing" outside of the class

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
print(Rules.washing_brushes("self"))
# OR
example_object = Rules()  # We created an object of the class, then can call Class Methods without arguments
print(example_object.washing_brushes())

class Dog():
  dog_time_dilation = 7
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
pipi_pitbull = Dog()# We created an object of the class, then can call Class Methods without arguments
pipi_pitbull.time_explanation()  # Prints "Dogs experience 7 years for every 1 human year."


# Create a class to calculate areas of circles
class Circle:
    pi = 3.14  # Pi Class Variable
    def area(self, radius):  # Calculates area by taking in radius as a paramter
        return Circle.pi * radius ** 2  # In order to interact with Class Variable, have to use ClassName.Variable

circle = Circle()  # Instantiate class object
pizza_area = circle.area(12 / 2)  # Call class method circle.area(with argument 12 / 2)
print(pizza_area)  # Prints 113.04
teaching_table_area = circle.area(36 / 2)  # Call class method circle.area(with argument 36 / 2)
print(teaching_table_area)  # Prints 1017.36
round_room_area = circle.area(11460 / 2)  # Call class method circle.area(with argument 11460 / 2)
print(round_room_area)  # Prints 103095306.0


# Create a class with a constructor example
class Circle:
    pi = 3.14
    def __init__(self, diameter):  # Constructor __init__ will take an argument for diameter and print a statement
        print("New circle with diameter: {}".format(diameter))

teaching_table = Circle(36)  # Prints "New circle with diameter: 36"


# Instance variable example:
class Store:
  pass
# Instantiate objects using Store() class
alternative_rocks = Store()
isabelles_ices = Store()
# Assign instance variables for each object
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# hasattr() & getattr() examples
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()  # Create object called attributeless that is instantiated from NoCustomAtrributes

try:
  attributeless.fake_attribute  # Doesnt exist so goes to except
except AttributeError:
  print("This text gets printed!")  # This gets printed
# hasattr() will either return True or False based on the attribute being looked for existing
hasattr(attributeless, "fake_attribute")  # checks object for attribute named "fake_attribute" & returns False
# getattr() will return the attribute being look for or a default attribute you define, in the below case 800
getattr(attributeless, "other_fake_attribute", 800)  # checks object for attribute, returns false so assigns 800


# hasattr() example, to find if a dataype includes the attribute "count" and if so to use it to count something
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for data_type in how_many_s:
  if hasattr(data_type, "count") == True:
    print(data_type.count("s"))


# Example of using "self" keyword to call another method within the class
class SearchEngineEntry():
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
# Call uses implied Self
print(codecademy.secure()  # prints "https://www.codecademy.com"
print(wikipedia.secure())  # prints "https://www.wikipedia.org"

# Example of using "self" keyword to call another method within the class
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2
    def circumference(self):
        return 2 * self.pi * self.radius

medium_pizza = Circle(12)  # Prints "Creating circle with diameter 12"
print(medium_pizza.circumference())  # Prints "37.68" as call implies Self
teaching_table = Circle(36)  # Prints "Creating circle with diameter 36"
print(teaching_table.circumference())  # Prints "113.04" as call implies Self
round_room = Circle(11460)  # Prints "Creating circle with diameter 11460"
print(round_room.circumference())  # Prints "35984.4" as call implies Self


# String Representation with __repr__ which converts "<__main__.Employee object at 0x104e88390>" to "Argus Filch"
class Employee():
  def __init__(self, name):
    self.name = name
argus = Employee("Argus Filch")
print(argus)  # Prints "<__main__.Employee object at 0x104e88390>"

class Employee():
  def __init__(self, name):
    self.name = name
  def __repr__(self):  # __repr__
    return self.name
argus = Employee("Argus Filch")
print(argus)  # Prints "Argus Filch"


# String representation with __repr__
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radius = diameter / 2
    def __repr__(self):
        return "Circle with radius {}".format(self.radius)
    def area(self):
        return self.pi * self.radius ** 2
    def circumference(self):
        return self.pi * 2 * self.radius

medium_pizza = Circle(12)
print(medium_pizza)  # Circle with radius 6.0
teaching_table = Circle(36)
print(teaching_table)  # Circle with radius 18.0
round_room = Circle(11460)
print(round_room)  # Circle with radius 5730.0


# Classes Exercise
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

class Grade:
    minimum_passing = 65
    def __init__(self, score):
        self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))