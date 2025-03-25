# Letter Counter (Part 1)
# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

# Words consist of any sequence of non-space characters.

# All of these examples should print True
# -we define `result` dict
# -split the str into words
# -iterate over words
# -get the len of each word
# -we want to have the len as the key
# -if it is not in the dict as a key, we add it and value will be 1
# -if it already is in the dict, just increase value by 1

# -return the `result` dict


def word_sizes(string):
    if string == '':
        return {}
    else:
        words = string.split(" ")
        result = {}
        for word in words:
            length_of_word = len(word)
            if length_of_word not in result:
                result[length_of_word] = 1
            else:
                result[length_of_word] += 1
        return result


string = 'Four score and sevenXXX.'
print(word_sizes(string))
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})



