# This is a comment

# This code below defines a function, formatted as "def namehere():" and anything under the function has to be indented
def loading_screen():
    print("This page is loading...")
    print("...page done loading")
loading_screen()


# The below function includes a parameter called "number", we specify the parameter when we call the function
def mult_two_add_three(number):
    print(number*2 + 3)
mult_two_add_three(5) # parameter specified is 5 and will be used in the function defined above


# The below function includes multiple parameters called "number, X, and Y".
def mult_x_add_y(number, x, y):
    print(number * x + y)
mult_x_add_y(5, 2, 3) # parameter specified is number=5, x=2, and y=3


# The below function starts with row_count=1000 but when functions called we change it to 10.
# Additionally, since we are calling a int in the print, we have to concatenate the int into a string with str()
def create_spreadsheet(title, row_count=1000):
    print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")
create_spreadsheet("Applications", row_count=10)


# The below function calculates age and stores/returns the calculation into variable "age"
# So age equals current_year minus birth_year and stores the age for later use when the function is called.
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
# Function generates equation 2018-1993=25, 25 gets stored in "age", then we return "age=25" into the new var my_age
my_age = calculate_age(2018, 1993)
# Function generates quation 2018-1953=65, 65 gets stored in "age", then we return "age=65" into the new var dads_age
dads_age = calculate_age(2018, 1953)
# Additionally, since we are calling a int in the print, we have to concatenate the int into a string with str()
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")


# Below is an example of doing multiple returns together, then creating multiple variables when calling the function
def get_boundaries(target, margin):
  low_limit = margin - target
  high_limit = margin + target
  return low_limit, high_limit
low, high = get_boundaries(100, 20)
# Additionally, since we are calling a int in the print, we have to concatenate the int into a string with str()
print("Low limit: " + str(low) + ", high limit: " + str(high))


# Example is a function called repeat_stuff, with two variable called "stuff" and "num_repeats" with a value of 10
# We will return the result of the equation stuff x num_repeats when the function repeat_stuff is called.
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats
# We created a variable called lyrics and it equals the function with the parameters defined as "Row " and 3.
# We additionally added the text string "Your boat" to the end of whatever the function produced.
lyrics = repeat_stuff("Row ", 3) + "Your Boat"
# We created a variable called song and it equals the function with the parameter of lyrics
song = repeat_stuff(lyrics)
print(song)


# A better song example would be below:
def lyrics(first_word, second_word, third_word):
    sentence = first_word + second_word + third_word
    return sentence
first_phrase = lyrics("Captain ", "Flurry ", "and his Henchmen!")
print(first_phrase)


# More Examples:

# average function here:
def average(num1, num2):
  return (num1 + num2) / 2
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


# tenth_power function here:
def tenth_power(num):
  return num ** 10
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


# introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


# square_root function here:
def square_root(num):
  return num ** 0.5
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


# tip function here:
def tip(total, percentage):
  return percentage / 100 * total
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


# win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num * 1)
  print(num * 2)
  print(num * 3)
  return num * 3
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


# dog_years function here:
def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


# remainder function here:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


# lots_of_math function here:
def lots_of_math(a, b, c, d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return ((a + b) * (c - d) % a)
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0


# bro_love function here:
def bro_love(person1, person2):
    return (person1 + " and " + person2 + " have a little bro love going on!")
# assign variable love output of bro_love function
print(bro_love("Dan", "Cody"))


def bro_love(person1, person2):
    return (person1 + " and " + person2 + " have a little bro love going on!")

print(bro_love("Dan", "Cody"))


# https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
# String formatters
print("Daniel has {} balloons.".format(10))
print("Andrew is not {} number of people's keeper".format(10))
print("Andrew is not {} or {} years old".format(1, 2))
print("Thanks for showing me examples {}. {}, and {} with regards to string format".format(1, 2, 3))

# Playing with return

def brolove(name1, name2):
    print(name1 + " and " + name2 + " have some bro love going on!")
    return name1 + " and " + name2 + " have some bro love going on!"
# will print the sentence and assign a variable x to the string returned
x = brolove("Dan", "Mat")
# will print the variable x which is the string taken from the return on brolove
print(x)

