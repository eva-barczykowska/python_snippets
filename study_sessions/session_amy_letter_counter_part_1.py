# Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

# Goal: Intake a list and return a list with the same number of elements and each element is the addition of the one(s) before it.
# input: list
# output: list

# empty list returns empty list
# E: input [14, 11, 7, 15, 20] output: [14, 25, 32, 47, 67]
# 14 + 11 = 25, 25 +7 = 32...

# D: list -> new list

# A: create a new list
# - iterate over the input
#   - the first element becomes the first elemnt of new_list
# -  add the next element to the previous element and add to the new_list
# return new_list

# def running_total(lst):
#     new_list = []
#     index = 0
#     for elem in lst:
#         if index == 0:
#             new_list.append(elem)
#         else:
#             sum = lst[index] + new_list[index -1]
#             new_list.append(sum)
#         index += 1
#     return new_list


# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# def running_total(lst):
#     new_list =[]
#     for idx, elem in enumerate(lst):
#         if idx == 0:
#             new_list.append(elem)
#         else:
#             sum = lst[idx] + new_list[idx - 1]
#             new_list.append(sum)
#     return new_list


# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# =========
# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

# Words consist of any sequence of non-space characters.
# All of these examples should print True

# function takes a str as an arg
# function returns a dict
# dict shows no of words of different sizes

# initialize dict counts
# split sentence into words
# look at every word in the list and find out its lengh this will be an int
# if that int already exists in the dict as a key, increase its value
# else use this int to create a key and point to to value 0
# return counts

# def word_sizes(sentence):
#     if sentence == "":
#        return {}

#     list_of_words = sentence.split(" ")
#     counts = {}
#     for word in list_of_words:
#         length_of_word = len(word)
#         if length_of_word in counts.keys():
#             counts[length_of_word] += 1
#         else:
#             counts[length_of_word] = 1
#     return counts


# string = 'Four score and seven.'
# print(word_sizes(string)) == {4: 1, 5: 1, 3: 1, 6: 1}

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

def word_sizes(sentence):
    # if sentence == "":
    #    return {}

    list_of_words = sentence.split(" ")
    counts = {}
    for word in list_of_words:
        length_of_word = len(word)
        if length_of_word == 0:
            continue
        elif length_of_word in counts.keys():
            counts[length_of_word] += 1
        else:
            counts[length_of_word] = 1
    return counts


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})