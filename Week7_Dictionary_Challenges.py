# Add together all the values found in a dictionary
def sum_values(my_dictionary):
    total = 0
    for i in my_dictionary.values():
        total += i
    return total
#print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))  # Prints 10
#print(sum_values({10:1, 100:2, 1000:3}))  # should print 6


# Add together all the values found in a dictionary if the values are even
def sum_even_values(my_dictionary):
    total = 0
    for i in my_dictionary.values():
        if i % 2 == 0:
            total += i
    return total
#print(sum_even_values({1:5, 2:2, 3:3}))  # should print 2
#print(sum_even_values({10:1, 100:2, 1000:3}))  # should print 2


# Add together all the values found in a dictionary if the keys are even
def sum_even_keys(my_dictionary):
    total = 0
    for i in my_dictionary:
        if i % 2 == 0:
            total += my_dictionary.get(i)
    return total

#print(sum_even_keys({1: 5, 2: 2, 3: 3}))  # should print 2
#print(sum_even_keys({10: 1, 100: 2, 1000: 3}))  # should print 6


# Add 10 to each existing value in dictionary
def add_ten(my_dictionary):
    for i in my_dictionary:
        my_dictionary[i] += 10
    return my_dictionary
#print(add_ten({1:5, 2:2, 3:3}))  # should print {1:15, 2:12, 3:13}
#print(add_ten({10:1, 100:2, 1000:3}))  # should print {10:11, 100:12, 1000:13}


# Checks if a value is a key in dictionary
def values_that_are_keys(my_dictionary):
    output = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            output.append(value)
    return output

#print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))  # should print [1, 4]
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))   # should print ["a"]


# Returns the highest value found in the dictionary
def max_value(my_dictionary):
    highest_value = 0
    for value in my_dictionary.values():
        if value > highest_value:
            highest_value = value
    return highest_value
#print(max_value({1:100, 2:1, 3:4, 4:10}))  # should print 1
#print(max_value({"a":100, "b":10, "c":1000}))  # should print "c"


# Returns the highest key based on highest value found in the dictionary
def max_key(my_dictionary):
    highest_value = 0
    highest_key = ""
    for key in my_dictionary:
        if my_dictionary.get(key) > highest_value:
            highest_value = my_dictionary.get(key)
            highest_key = key
    return highest_key
#print(max_key({1:100, 2:1, 3:4, 4:10}))  # should print 1
#print(max_key({"a":100, "b":10, "c":1000}))  # should print "c"


# Create a dictionary using a list, keys are the items in the list and the values are their lengths
def word_length_dictionary(words):
    dictionary = {}
    for word in words:
        dictionary[word] = len(word)
    return dictionary
#print(word_length_dictionary(["apple", "dog", "cat"]))  # should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))  # should print {"a": 1, "": 0}


# Count how many times a word shows up in a list, add it to a dictionary as the key with the count as the value
def frequency_dictionary(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
#print(frequency_dictionary(["apple", "apple", "cat", 1]))  # should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))  # should print {0:5}


# Return the number of unique values found in the dictionary
def unique_values(my_dictionary):
    values_found = []
    [values_found.append(value) for value in my_dictionary.values() if value not in values_found]
    return len(values_found)
#print(unique_values({0:3, 1:1, 4:1, 5:3}))  # should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))  # should print 1


# Count first letter
def count_first_letter(names):
    #dictionary = {last_name[0]: len(first_name) for (last_name, first_name) in names.items()}
    dictionary = {}
    for key in names:
        if key[0] in dictionary:  # Dont forget that we want to specifically look for the first character key so key[0]
            dictionary[key[0]] += len(names.get(key))
        else:
            dictionary[key[0]] = len(names.get(key))
    return dictionary
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))  # should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))  # should print {"S": 7}
