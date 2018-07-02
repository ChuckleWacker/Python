greeting = "Hello World"
print(greeting)  # Starts Normal Case
print(greeting.upper())  # Prints Upper Case
print(greeting.lower())  # Prints Lower Case
print(greeting.title())  # Prints Proper Case, first letter of each word is capitalized
print(greeting.split())  # Prints Split into a list
print(" ".join(["Hello", "World"]))  # Joins list together
print("Hello World".replace("H", "J"))  # Prints Jello World as we replaced a letter
print("     Hello World     ".strip())  # Prints without the blank spaces before or after
print("{} {}".format("Hello", "World"))  # Formats str/int into string

# Fixing existing strings with Title Case and Upper Case
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()
print(poem_title_fixed)
print(poem_author_fixed)


# Splitting strings
line_one = "The sky has given over"
line_one_words = line_one.split()  # Without an argument, defaults to splitting by spaces
line_one_words_arg = line_one.split("has")  # Splits using "has"
print(line_one_words)  # Prints ['The', 'sky', 'has', 'given', 'over']
print(line_one_words_arg)  # Prints ['The sky ', ' given over']


# Function takes a list and outputs the last word in each index.
example = ["Hello there, Dan.", "Have a nice day!", "Let's learn some programming"]
def find_last_word(sentences):
    last_words = []
    for word in sentences:
        last_words.append(word.split()[-1])
    return last_words
assert find_last_word(example) == ["Dan.", "day!", "programming"]

new_var = find_last_word(example)  # Assigned the output of the function to a new variable
print(new_var)


# Splitting a string by lines using split("\n")
example = """First Line
Second Line
Third Line"""
example_split = example.split("\n")
print(example_split)


# Joining a list into a single string
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)  # " " as the joining delimiter will combine each with a space
print(reapers_line_one)


# Joining a list into a single string
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = "\n".join(reapers_line_one_words)  # "\n" as the joining delimiter will combine each as a new line
print(reapers_line_one)



love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]  # List comprehension to strip from list
print(love_maybe_lines_stripped)  # prints list without spaces
love_maybe_full = "\n".join(love_maybe_lines_stripped)  # Combine list, each index will be its own line
print(love_maybe_full)


# Replace Function example
some_string = "Daniel Boggs and Kiara Howe are married"
some_string_fixed = some_string.replace("Howe", "Boggs")  # Looking for "Howe" and replacing it with "Boggs"
print(some_string_fixed)  # Prints "Daniel Boggs and Kiara Boggs are married"

# Replace Function example
friends = "Dan and Body"
friends_fixed = friends.replace("Body", "Cody")
print(friends_fixed)  # Prints "Dan and Cody"


# Find Function example
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)  # Prints 20 as that is the where the d in disown first appears in the index


# .Format Function example
def poem_title_card(poet, title):
    return "The poem \"{}\" is written by {}.".format(title, poet)  # Will return the poet and title plugged in.


# .Format Function example where you list keywords as they relate to the arguments called out later, you can
# ignore the order of variable using this method.
def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)


# .Format Function example with keywords and variables
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}."\
        .format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
    return poem_desc
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)


# Full String Method Examples
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(",")
highlighted_poems_stripped = [poems.strip() for poems in highlighted_poems_list]
highlighted_poems_details = []

for poems in highlighted_poems_stripped:
    highlighted_poems_details.append(poems.split(":"))
#print(highlighted_poems_details)
titles = []
poets = []
dates = []
for poems in highlighted_poems_details:
    titles.append(poems[0])
    poets.append(poems[1])
    dates.append(poems[2])
for i in range(len(titles)):
    print("The poem {titles} was published by {poets} in {dates}".format(titles=titles[i], poets=poets[i],
                                                                         dates=dates[i]))
