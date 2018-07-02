# Boolean Operators
# Equals: ==
# Not Equals: !=
# Greater Than: >
# Less Than: <
# Greater Than or Equal To: >=
# Less than of Equal To: <=

1 == 1   # Equals
2 != 4   # Not Equals
3 == 5   # Equals
"7" == 7 # Equals

(5 * 2) - 1 == 8 + 1  # True
13 - 6 != (3 * 2) + 1 # False. 7 equals 7
3 * (2 - 1) == 4 - 1  # True

my_baby_bool = "true"
print(type(my_baby_bool)) # Class equals Str since we defined a string for the variable

my_baby_bool_two = True
print(type(my_baby_bool_two)) # Class equals Bool since we defined True or False as the variable


# If Statement to evaluate is 1 equals 2-1, since it does we "THEN" print=ed a string response
if 1 == 2 - 1:
    print("The answer is 1")


# Defined function that checks if user_name equals either "Dave" or "Mat"
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "Mat":
        return "I know it is you Mat! Go away!"
    else: return "You are clear to login, since you are neither Dave or Mat."
# Enter a user name here, make sure to make it a string
user_name = "Dan"
print(dave_check(user_name))


# Age Checking Function
def age_check(age):
    if age >= 13:
        print("You are over the age of 13, so you can watch PG13 movies.")
        return True
    else:
        print("You must be 13 yrs or older to be watching this movie!")
        return False
age_check(10)


# Greater Than Function
def greater_than(x, y):
    if x > y:
        return x
    if x < y:
        return y
    if x == y:
        return "These numbers are the same"
greater_than(1, 1)


# Graduation Req Function
def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    elif (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    elif (credits >= 120) and not (gpa >= 2.0):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."
print(graduation_reqs(2.0, 120))
print(graduation_reqs(2.0, 100))
print(graduation_reqs(1.0, 120))
print(graduation_reqs(1.0, 100))

# Grade calculator Function
def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  else:
    return "F"


# College Applicant Selector Function
def applicant_selector(gpa, ps_score, ec_count):
    if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
        return "This applicant should be accepted."
    elif gpa >= 3.0 and ps_score >= 90 and not ec_count >= 3:
        return "This applicant should be given an in-person interview."
    else:
        return "This applicant should be rejected."


# College Applicant Selector Function
def student(gpa, credits):
    if gpa >= 2.5 and credits >= 120:
        print("Student's gpa of {} and credits of {} are sufficient for graduation".format(gpa, credits))
    elif gpa >= 2.5 and not credits >= 120:
        print("Student's credits of {} is too low for graduation".format(credits))
    elif not gpa >= 2.5 and credits >= 120:
        print("Student's gpa of {} is too low for graduation".format(gpa))
    else:
        print("Student's gpa of {} and credits of {} are too low for graduation".format(gpa, credits))
student(1.6, 110)


# Countdown to boardgaming Function
def boardgame_countdown(days):
    if days <= 1:
        print("Boardgaming is coming!")
    if days > 1:
        print("T-Minus {} days until Boardgaming!".format(days))
boardgame_countdown(1)


# Checks the range of a number Function
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
      return True
    else:
      return False
print(in_range(10, 10, 10))  # should print True
print(in_range(5, 10, 20))  # should print False


# Movie Rating Function
def movie_review(rating):
    if rating <= 5:
      return "Avoid at all costs!"
    if rating > 5 and rating < 9:
      return "This one was fun."
    if rating >= 9:
      return "Outstanding!"
print(movie_review(9))  # should print "Outstanding!"
print(movie_review(4))  # should print "Avoid at all costs!"
print(movie_review(6))  # should print "This one was fun."


# Is Number Higher Function
def twice_as_large(num1, num2):
    if num1 > num2 * 2:
      return True
    else:
      return False
print(twice_as_large(10, 5))  # should print False
print(twice_as_large(11, 5))  # should print True


# Is Base Raised to Exponent Greater than 5000 Function
def large_power(base, exponent):
    if base ** exponent > 5000:
      return True
    else:
      return False
print(large_power(2, 13))  # should print True
print(large_power(2, 12))  # should print False


# Which Number is Greater Function
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      return num1
    elif num2 > num3 and num2 > num1:
      return num2
    elif num3 > num2 and num3 > num1:
      return num3
    else:
      return "It's a tie!"
print(max_num(-10, 0, 10))  # should print 10
print(max_num(-10, 5, -30))  # should print 5
print(max_num(-5, -10, -10))  # should print -5
print(max_num(2, 3, 3))  # should print "It's a tie!"


# Budget Function
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
      return True
    else:
      return False
print(over_budget(100, 20, 30, 10, 40))  # should print False
print(over_budget(80, 20, 30, 10, 30))  # should print True


# Not Equal Function
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
      return True
    else:
      return False
print(not_sum_to_ten(9, -1))  # should print True
print(not_sum_to_ten(9, 1))  # should print False
print(not_sum_to_ten(5,5))  # should print False


# Name Compare Function
def same_name(your_name, my_name):
    if your_name == my_name:
      return True
    else:
      return False
print(same_name("Colby", "Colby"))  # should print True
print(same_name("Tina", "Amber"))  # should print False
