# Create a dictionary, consists of a key: value (which can be str, int, list). Lists just cant be keys.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}


# Create an empty dictionary for later use
my_empty_dictionary = {}


# Single Add/Update to dictionary
animals_in_zoo = {}  # Empty dictionary
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)  # {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}


# Multiple Add/Update to dictionary
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
sensors.update({"pantry": 22, "bathroom": 16})  # Add key=pantry: value=22 to dictionary
num_cameras.update({"living room": 3, "closet": 4})
print(sensors)  # {'living room': 21, 'pantry': 22, 'kitchen': 23, 'bedroom': 20, 'bathroom': 16}
print(num_cameras)  # {'backyard': 6, 'garage': 2, 'driveway': 1, 'living room': 3, 'closet': 4}


# Combine to lists into a dictionary
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# Short way
drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)  # {'chai': 40, 'espresso': 64, 'drip': 120, 'decaf': 0}
# Long way by zipping to a variable
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)  # <zip object at 0x7f132eb2f408>
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)  # {'chai': 40, 'espresso': 64, 'drip': 120, 'decaf': 0}


# Practicing all the concepts above
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)  # Creates dictionary
plays.update({"Purple Haze": 1})
print(plays)  # Adds "Purple Haze": 1 to dictionary
plays["Respect"] += 5
print(plays)  # Updates Key="Respect" value to include + 5
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)  # Create a dictionary with a value of another dictionary and a value with an empty dictionary


#  Accessing data by keys using If / Else
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])  # Prints ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])  # Prints ['Aries', 'Leo', 'Sagittarius']

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# zodiac_elements["energy"] = "Not a Zodiac element"  # Commented out to force Key Error as not existing
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Should not print as "energy" is not in the dictionary as a key
else:
    print(zodiac_elements["air"])  # Should print instead unless we uncomment zodiac_elements["energy"] on line 60


# Accessing data by keys using Try / Except, include Error Handling with Except
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
# caffeine_level['matcha'] = 30
try:
    print(caffeine_level['matcha'])  # With match not in the dictionary, this will fail and generate KeyError
except KeyError:  # We define that when KeyError comes up to do something else
    print("Unknown Caffeine Level")  # So we print "Unknown Caffeine Level" in place of the KeyError


# Getting data to assign to a variable, if the data doesnt exist it proactively provides a value to use
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)  # Because teraCoder existed, it used the value found 100019
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)  # Because superStackSmash doesnt exist, it used the proactive number 100000 defined


# Deleting data from a dictionary, can additionally use the value while removing it as shown below
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)  # adds the value of "stamina grains" to health_points
print(health_points, available_items)  # Health is now 35. "stamina grains" has been removed from available_items
health_points += available_items.pop("power stew", 0)  # add the value of "power stew" to health_points
print(health_points, available_items)  # Health is now 65. "power stew" has been removed from available_items
health_points += available_items.pop("mystic bread", 0)  # "mystic bread" doesnt exist so adds 0 instead of erroring
print(health_points)  # Final health is 65


# Create lists from a dictionary Keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()  # Is an iterable list that can be used in a for loop. ex. for i in variable.keys()
print(users)  # Prints as dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
lessons = list(num_exercises)  # is a standard list
print(lessons)  # Prints as ['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries']


# Create lists from dictionary Values
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for i in num_exercises.values():
  total_exercises += i
print(total_exercises)  # Prints 115 which is the total of all values in the dictionary
total_exercises_list1 = num_exercises.values()  # Is an iterable list that can be used in a for loop as shown above
print(total_exercises_list1)  # Prints as dict_values([10, 13, 15, 22, 19, 18, 18])
total_exercises_list2 = list(num_exercises.values())  # is a standard list
print(total_exercises_list2)  # Prints as [10, 13, 15, 22, 19, 18, 18]


# Create tuple, get all items from a dictionary (key, value,
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37,
                           "Aerospace Engineer": 9}
print(pct_women_in_occupation.items())  # Prints as dict_items([('CEO', 28), ('Engineering Manager', 9),
# ('Pharmacist', 58), ('Physician', 40), ('Lawyer', 37), ('Aerospace Engineer', 9)])
for key, value in pct_women_in_occupation.items():  # Since .items() creates an iterable list, can be used in For loop
  print("Women make up {} percent of {}s.".format(value, key))  # Prints as "Women make up 28 percent of CEOs"... etc.


# Practice with Dictionary concepts
tarot = {1: "The Magician", 2: "The High Priestess", 3:	"The Empress", 4: "The Emperor", 5:	"The Hierophant",
         6:	"The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10:	"Wheel of Fortune", 11:	"Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17:	"The Star",
         18: "The Moon", 19: "The Sun", 20:	"Judgement", 21: "The World", 22: "The Fool"}
spread = {}  # Created empty dictionary
spread["past"] = tarot.pop(13)
print(spread)  # Adds "past": "Death" to spread dictionary
spread["present"] = tarot.pop(22)
print(spread)  # Adds "present": "The Fool" to spread dictionary
spread["future"] = tarot.pop(10)
print(spread)  # Adds "future": "Wheel of Fortune" to spread dictionary
for key, value in spread.items():
  print("Your {} is the {} card.".format(key, value))
# Prints as: Your present is the The Fool card.
# Prints as: Your past is the Death card.
# Prints as: Your future is the Wheel of Fortune card.
