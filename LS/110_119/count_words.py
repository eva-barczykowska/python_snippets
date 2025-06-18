# Letter Counter (Part 1)
# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes. Words consist of any sequence of non-space characters.

# Problem: function that:
# input: a string of zero or more space separated words
# output: a dictionary that shows the number of words of words and their sizes
# rules:
#punctuation counts to the overall counts

#Example: "Hello, World" ==? {6:1, 5:1}
#Data structure: Dictionary

#Algorithm:
#    - initialize an empty dictionary
#    - for loop 1: iterate over a List
# - for loop 2: iterate over element in a list
# - update count of the character
# result[number] = result.get(number, 0) + 1
# - store character in a dictionary
#     - return list


# def word_sizes(text):

#     result = {}
#     string_list = text.split()
#     for element in string_list:
#         result[len(element)] = result.get(len(element), 0) + 1
#     print(result)
#     return result




# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})
# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})
# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})
# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})
# print(word_sizes('') == {})

# Letter Counter (Part 2)
# Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

# All of these examples should print True

"""
P:
we have to return a dictionary where key says how many letters are in a word
value says how many words we have of that count
"it's" -> {3:1}

DS:
-list
-dict

A:
-initialize dictionary
-initialize count to 0
-split the list into words
-iterate over each character in each word
-is the char I'm iterating over isalpha, add 1 to the count
-when finished iterating over 1 word, check the dict
-if a key with the number of characters in this word DOESNT EXIST
--create it
---else
--add 1 to the value for that existing key
--reset the counter

"""

def word_sizes(string):
    result = {}
    string = string.split()

    for one_word in string:
        count = 0
        for one_char in one_word:
            if one_char.isalpha():
                count += 1
        if count in result:
            result[count] += 1
        else:
            result[count] = 1

    return result





string = 'Four score and seven.'
print(word_sizes(string)) #== {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# split it in 2 functions, one deals with the word, the other one creates the result dictionary

def count_chars(word):
    count = 0

    for char in word:
        if char.isalpha():
            count += 1
    return count

word = "What's"
print(count_chars(word))

def word_sizes(string):
    result = {}
    string = string.split()

    for one_word in string:
        count = count_chars(one_word)

        if count in result:
            result[count] += 1
        else:
            result[count] = 1

    return result



string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print()
# another way when passing a function to a function
"""
A:
-initialize dictionary
-initialize count to 0
-map words to a list of numbers, exclude non-alphabet chars
-create a hash out of that list
--return that hash
"""

from collections import Counter
def word_sizes(string):
    result = {}
    temp = []
    filtered_words = list((word for word in string.split() if word.isalpha())) # get rid of non-alphabet chars
    # mapped_to_nums = map(filtered_words, len)
    # for w in filtered_words:
    #     temp.append(len(w))
    counts = Counter(filtered_words)
    # print(counts) # Counter({'Four': 1, 'score': 1, 'and': 1})
    for k, v in counts.items():
        if len(k) in result:
            result[len(k)] += 1
        else:
            result[len(k)] = 1

    return result



string = 'Four score and seven.'
print(word_sizes(string))# == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})
#
# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})
#
# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})
#
# print(word_sizes('') == {})

# example of how to use collections.Counter / similar to tally in Ruby
# First, import the Counter class

# print("counter------------------")
# from collections import Counter
#
# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
#
# # Create a Counter instance from the list
# counts = Counter(fruits)
#
# # It looks and acts like a dictionary
# print(counts) # => Counter({'apple': 3, 'banana': 2, 'orange': 1})
# print(type(counts))
#
# print(counts["apple"])
# # => 3




