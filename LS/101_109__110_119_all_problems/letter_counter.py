'''
Write a function that takes a string consisting of zero
or more space-separated words and returns a dictionary that shows the number of words
of different sizes.

Words consist of any sequence of non-space characters.

PEDAC
Problem
-input: a string of zero or more space separated words
-output: a dictionary that shows the number of words of words and their sizes
-i see that special chars are counted too

A:
-split the string into words (on a space)
-initialize an empty dictionary to store the word sizes
-for each word, check its size
-check if the size is already in the dictionary as a key, if it is, increment its value
-if it is not, create it as a key and point to the value 1

-return the dictionary
'''

def word_sizes(string):
    words = string.split()
    result = {}
    for word in words:
        print(f"len of {word} is {len(word)}")
        if len(word) in result:
            result[len(word)] += 1
        else:
            result[len(word)] = 1

    return result


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {}) # split results in [] so LOOP DOES NOT RUN -- dictionary is empty
# if we split an empty string on a space, we are getting an empty list, with a space inside?

print(len(''.split(" ")))

print("modify solution to exclude special characters")
print("---------------")

def word_sizes(string):
    words = string.split()
    result = {}

    for word in words:
        counter = 0
        for char in word:
            if char.isalpha():
                counter += 1
        if counter in result:
            result[counter] += 1
        else:
            result[counter] = 1

    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})