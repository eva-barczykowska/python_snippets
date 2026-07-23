# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started

# print(scramble_words('professionals')) #'paefilnoorsss'
# print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))
#"you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."



# Problem
# -the func has to do the following
# -return the arg string BUT
# -first and last letter stay the same
# (effectively the change is for words more than 3 characters long)
# -the middle part is alphabetically sorted
# -punctuation remains in its original place


# Examples
# print(scramble_words('professionals')) #'paefilnoorsss'
# print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))
#"you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."

# Algorithm
# -prepare a func for each word, process_word
# -it checks arg's len
# -if len > 3:
# -init new_str
# -check for special chars, save the index of special char in a word (there will be only 1 special char as per examples)
# -remove special char
# -split into beginning, middle end
# -sort the middle alphabetically
# -put back beginning, middle, end
# -insert special char at the saved index position
# -return the word

# -else just return the word

# -main function, process_string
# -if no spaces, just process_word and return it
# -if spaces, split on a space and invoke process_word on each word
# -append the return value to the list
# -convert the list back into str
# -return



def get_special_char(word):
    special_char = "" #
    for char in word:
        if not char.isalnum():
            special_char = char
    return special_char

def get_special_char_index(word, special_char):
    return word.index(special_char)

def clean_word(word):
    cleaned_word = ""
    for char in word:
        if char.isalnum():
            cleaned_word += char

    return cleaned_word


def process_word(word):
    if len(word) < 4:
        return word
    elif word.isalnum():
        beginning, middle, end = word[0], word[1:-1], word[-1]
        sorted_middle = sorted(list(middle))
        word = list(beginning) + sorted_middle + list(end)
        return "".join(word)
    elif not word.isalnum():
        special_char = get_special_char(word)
        special_char_idx = get_special_char_index(word, special_char)
        cleaned_word = clean_word(word)
        beginning = list(cleaned_word[0])
        middle = list(cleaned_word[1:-1])
        end = list(cleaned_word[-1])
        sorted_middle = sorted(middle)
        word = beginning + sorted_middle + end
        word.insert(special_char_idx, special_char)
        return "".join(word)
# how to put my special char in the place that it was
# I have index, I have char

def scramble_words(s):
    if " " not in s:
        result = process_word(s)
        return result
    else:
        list_of_words = s.split(" ")
        result = []
        for one_word in list_of_words:
            processed_word = process_word(one_word)
            result.append(processed_word)

        return " ".join(result)

# print(scramble_words('professionals')) #'paefilnoorsss'
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
# "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
# word = "he's"
# special_char = get_special_char(word)
# print(get_special_char_index(word, special_char))


# Asked AI to give me a simpler/better solution:

def scramble_word(word):
    # Handle short words
    if len(word) < 4:
        return word

    # Separate punctuation (assume one punctuation at most)
    punct = ''
    punct_index = -1
    for i, char in enumerate(word):
        if not char.isalnum():
            punct = char
            punct_index = i
            word = word.replace(char, '')
            break

    # Scramble if still long enough
    if len(word) < 4:
        scrambled = word
    else:
        first, middle, last = word[0], sorted(word[1:-1]), word[-1]
        scrambled = first + ''.join(middle) + last

    # Reinsert punctuation if any
    if punct:
        scrambled = scrambled[:punct_index] + punct + scrambled[punct_index:]

    return scrambled

def scramble_words(text):
    return ' '.join(scramble_word(word) for word in text.split())

print(scramble_words('professionals') == 'paefilnoorsss')
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
