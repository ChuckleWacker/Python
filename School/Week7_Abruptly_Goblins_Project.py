# ABRUPTLY GOBLINS PLANNER

#######################################################################################################################
# FUNCTIONS:
#######################################################################################################################
# Function to update gamers list
def add_gamer(gamer, gamers_list):
    # gamer.get checks if the gamer parameters being pass includes "name" and "availability"
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("""Gamer missing proper key names "name" and/or "availability" in parameter included, please correct!""")
        print(gamer)


# Function to build a dictionary of: Keys=Days, Values=0 to be used later to count gamers interests
def build_daily_frequency_table():
    return {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}
# Function to calculate available days, takes gamers "availability" and adds a +1 to dict "available_frequency"
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:  # Iterates through each gamer
        for availability in gamer.get("availability"):  # Iterates through "availability" key
            if availability in available_frequency:  # If "availability" key also exists in dict "available_frequency"
                available_frequency[availability] += 1  # Update "available_frequency" key/value with +1


# Function to find night with highest availability
def find_best_night(availability_table):
    day = ""
    count = 0
    for availability in availability_table:
            if availability_table.get(availability) > count:  # dict.get will return the values of the key
                count = availability_table.get(availability)
                day = availability
    return day


# Function for who's available on "x" day
def available_on_night(gamers_list, day):
    names = []
    for gamer in gamers_list:  # Iterates through each gamer
        for availability in gamer.get("availability"):  # Iterates through "availability" key
            if availability == day:  # If "availability" key equals "day" parameter
                names.append(gamer.get("name"))  # Append name of gamer with gamer.get("name") as the key
    return names


# Function to send email
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:  # Iterate through gamers on parameter "gamers_who_can_attend"
        print("""Dear {}, The Sorcery Society is hosting a game of "{}" on {} night.""".format(gamer, game, day))


#######################################################################################################################
# WORKFLOW
#######################################################################################################################
# 1. Create our gamers list, populating gamers list with user data
gamers = []
add_gamer({"name": "Kimberly", "availability": ["Mondays", "Tuesdays", "Fridays"]}, gamers)
add_gamer({"name": "Thomas Nelson", "availability": ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({"name": "Joyce Sellers", "availability": ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({"name": "Michelle Reyes", "availability": ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({"name": "Stephen Adams", "availability": ["Thursday", "Saturday"]}, gamers)
add_gamer({"name": "Joanne Lynn", "availability": ["Monday", "Thursday"]}, gamers)
add_gamer({"name": "Latasha Bryan", "availability": ["Monday", "Sunday"]}, gamers)
add_gamer({"name": "Crystal Brewer", "availability": ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({"name": "James Barnes Jr.", "availability": ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({"name": "Michel Trujillo", "availability": ["Monday", "Tuesday", "Wednesday"]}, gamers)
print("GAMER'S LIST:", gamers)  # Check that gamer list populated

# 2. Find our first best game night to host "Abruptly Goblins!"
# Call function "build_daily_table to build our dictionary counter of key=days, values=num of available gamers
first_night_availability = build_daily_frequency_table()
# Call function "calculate_availability" to populate our dictionary counter with days users are available
calculate_availability(gamers, first_night_availability)
print("WEEKLY COUNT:", first_night_availability)
# Call function "find_best_night" to determine which night has the most availability
game_night = find_best_night(first_night_availability)
print("BEST GAME NIGHT:", game_night)  # Should print Thursday based on sample data
# Call function "available_on_night" to generate list of those whom can attend
attending_game_night = available_on_night(gamers, game_night)
print("ATTENDING GAME NIGHT:", attending_game_night)
# Call function "send_email" to send emails
send_email(attending_game_night, game_night, "Abruptly Goblin!")

print()  # Empty Line
print()  # Empty Line

# 3. Find our second best game night to host "Abruptly Goblins!"
# Create a list of those who couldn't attend
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
# Call function "build_daily_table to build our dictionary counter of key=days, values=num of available gamers
second_night_availability = build_daily_frequency_table()
# Call function "calculate_availability" to populate our dictionary counter with days users are available
calculate_availability(unable_to_attend_best_night, second_night_availability)
print("WEEKLY COUNT:", second_night_availability)
# Call function "find_best_night" to determine which night has the most availability
game_night2 = find_best_night(second_night_availability)
print("SECOND BEST GAME NIGHT:", game_night2)  # Should print Monday based on sample data
# Call function "available_on_night" to generate list of those whom can attend
available_second_game_night = available_on_night(gamers, game_night2)
print("ATTENDING GAME NIGHT:", available_second_game_night)
# Call function "send_email" to send emails
send_email(available_second_game_night, game_night2, "Abruptly Goblins!")
