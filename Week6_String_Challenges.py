# Function counts how many unique letters are in a word
def unique_english_letters(word):
    temp = []
    for letter in word:
        if letter not in temp:
            temp.append(letter)
    return int(len(temp))
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))


# Function counts how many times a specific letter shows up in a word
def count_char_x(word, x):
    count = 0
    for i in word:
        if i == x:
            count += 1
    return count
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))


# Function counts how many times a specific word shows up in a word
def count_multi_char_x(word, x):
    splits = word.split(x)
    return(len(splits)-1)
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))


# Function returns the substring of characters between Start and End
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return(word[start_ind + 1:end_ind])
    return word
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))


# Function determines if a word in a phrase is so many characters long
def x_length_words(sentence, x):
    sentence_list = sentence.split()
    for i in sentence_list:
        while len(i) >= x:
            return True
        else:
            return False
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))


# Function checks if word shows up in a phrase, whether phrase is all Upper / Lower / Title cased
def check_for_name(sentence, name):
    if name in sentence.title():
        return True
    elif name in sentence.upper():
        return True
    elif name in sentence.lower():
        return True
    else:
        return False
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))


# Function returns every other character of a string
def every_other_letter(word):
    return word[::2]
print(every_other_letter("Codecademy"))  # should print Cdcdm
print(every_other_letter("Hello world!"))  # should print Hlowrd
print(every_other_letter(""))  # should print nothing


# Function returns the string completely backwards
def reverse_string(word):
    return word[::-1]
print(reverse_string("Codecademy"))  # should print ymedacedoC
print(reverse_string("Hello world!"))  # should print !dlrow olleH
print(reverse_string(""))  # should print


# Function flips the first character between two words
def make_spoonerism(word1, word2):
    return word2[:1] + word1[1:] + " " + word1[:1] + word2[1:]
print(make_spoonerism("Codecademy", "Learn"))  # should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))  # should print wello Horld!
print(make_spoonerism("a", "b"))  # should print b a


# Function adds exclamation points if string is not 20 characters long, keeps adding until string is 20 characters long
# If string is already 20+ characters, it just returns the string.
def add_exclamation(word):
    if len(word) >= 20:
        return word
    elif len(word) < 20:
        while len(word) < 20:
            word = word + "!"
        return word
print(add_exclamation("Codecademy"))  # should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))  # should print Codecademy is the best place to learn
