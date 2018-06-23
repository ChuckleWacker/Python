# SCRABBLE GAME SCORER

letters = [letter.upper() for letter in ["a", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                                         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}


# Create a dictionary by combining the following lists: letters and points
letter_to_points = {key: value for key, value in zip(letters, points)}
# Add key, value to dictionary
letter_to_points[" "] = 0  # Added key-" ": value-0 to dictionary


# Function adds up the points for each letter in a word and returns the total
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)  # Use dictionary and .get the letter, else use 0
    return point_total


# Function tally's player word totals and adds their name/score to the empty dictionary "player_to_points"
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)  # Call function score_word to add the word's points
        player_to_points[player] = player_points  # Add players name as key, & player_points as value


# Function that takes in a player and a word, and adds the word to the list of words they've played
def play_word(player, word):
    player_to_words[player].append(word)  # Adds word to players dictionary values
    update_point_totals()  # Calls function to update scores

# Test adding new words to players respective value lists
play_word("player1", "NEW")  # Test adding word "NEW" which should make player1 score now 38
play_word("Prof Reader", "ZOO")

# Print total score
print(player_to_points)  # Prints {'Lexi Con': 31, 'Prof Reader': 31, 'player1': 38, 'wordNerd': 32}
