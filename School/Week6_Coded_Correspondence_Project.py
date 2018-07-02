# Coder/Decoder for string messages project

alphabet = ("abcdefghijklmnopqrstuvwxyz")
punctuation = ".,?'! "
decode_cipher = {"q": "a", "r": "b", "s": "c", "t": "d", "u": "e", "v": "f", "w": "g", "x": "h", "y": "i", "z": "j",
                 "a": "k", "b": "l", "c": "m", "d": "n", "e": "o", "f": "p", "g": "q", "h": "r", "i": "s", "j": "t",
                 "k": "u", "l": "v", "m": "w", "n": "x", "o": "y", "p": "z"}
encode_cipher = {"a": "q", "b": "r", "c": "s", "d": "t", "e": "u", "f": "v", "g": "w", "h": "x", "i": "y", "j": "z",
                 "k": "a", "l": "b", "m": "c", "n": "d", "o": "e", "p": "f", "q": "g", "r": "h", "s": "i", "t": "j",
                 "u": "k", "v": "l", "w": "m", "x": "n", "y": "o", "z": "p"}

message_1 = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q 
cuiiqwu rqsa myjx jxu iqcu evviuj!"""
message_2 = "i got your message, excellent choice of encryption by using the caeser shift!"
message_3 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message_4 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
message_5 = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx 
by px ptgm mh dxxi hnk fxlltzxl ltyx."""
message_6 = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"
message_7 = "this last message was tricky using the vigenere shift!"

# Function decodes a phrase using vigenere shift, uses a keyword to decode.
def decoder_vigenere(phrase, keyword):
    keyword_repeated = ""
    while len(keyword_repeated) < len(phrase):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(phrase)]
    translated_message = ""
    for i in range(0, len(phrase)):
        if not phrase[i] in punctuation:
            ln = alphabet.find(phrase[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += phrase[i]
    print(translated_message)


# Function emcodes a phrase using vigenere shift, uses a keyword to encode.
def encoder_vigenere(phrase, keyword):
    keyword_repeated = ""
    while len(keyword_repeated) < len(phrase):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(phrase)]
    translated_message = ""
    for i in range(0, len(phrase)):
        if phrase[i] not in punctuation:
            ln = alphabet.find(phrase[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += phrase[i]
    print(translated_message)


# Function decodes a phrase using caesar shift. Includes ability to specify offset.
def decoder_new(phrase, offset):
    decode_message = ""
    for character in phrase:
        if not character in punctuation:
            index = alphabet.find(character)
            decode_message += alphabet[(index + offset) % 26]
        else:
            decode_message += character
    print(decode_message)


# Function encodes a phrase using caesar shift. Includes ability to specify offset.
def encoder_new(phrase, offset):
    decode_message = ""
    for character in phrase:
        if not character in punctuation:
            index = alphabet.find(character)
            decode_message += alphabet[(index - offset) % 26]
        else:
            decode_message += character
    print(decode_message)


# Function decodes a phrase using dictionary already set with an offset of 10 using caeser shift
def decoder(phrase):
    decode_message = ""
    for character in phrase:
        if character in decode_cipher:
            decode_message += decode_cipher[character]
        else:
            decode_message += character
    print(decode_message)


# Function encodes a phrase using dictionary already set with an offset of 10 using caeser shift
def encoder(phrase):
    encode_message = ""
    for character in phrase:
        if character in encode_cipher:
            encode_message += encode_cipher[character]
        else:
            encode_message += character
    print(encode_message)


# Message should print: "hey there! this is an example of a caesar cipher. were you able to decode it?
# i hope so! send me a message back with the same offset!"
print("Message Number 1: ")
decoder(message_1)

# Message should print: "y wej oekh cuiiqwu, unsubbudj sxeysu ev udshofjyed ro kiydw jxu squiuh ixyvj!"
print("Message Number 2: ")
encoder(message_2)

# Message should print: "the offset for the second message is fourteen."
print("Message Number 3: ")
decoder(message_3)

# Message should print: "performing multiple caesar ciphers to code your messages is even more secure!"
print("Message Number 4: ")
decoder_new(message_4, 14)

# Cycle through coded message with every possible offset to determine the offset in use. In this case it is 7
print("Cycling through all offsets to determine which is in use: ")
for i in range(1, 26):
    print("Offset: {}".format(i))
    decoder_new(message_5, i)

# Message should print: "computers have rendered all of these old ciphers as obsolete. we'll have to really step up
# our game if we want to keep our messages safe."
print("Message Number 5: ")
decoder_new(message_5, 7)

# Message should print: "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
print("Message Number 6: ")
decoder_vigenere(message_6, "friends")

# Message should print: "oqao iinc irpavpw jxa cjephg dkead oqw ifozwwnr acrxp!"
print("Message Number 7: ")
encoder_vigenere(message_7, "friends")
