"""
Write a function that takes a string as an argument and groups the number of times each character appears in the string as a dictionary sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore spaces, special characters, and count uppercase letters as lowercase ones. Note: Good to revisit for sorting practice.
P:
sort letters descending, key is number of occurrences, values is letter(s) in a list
get rid of punctuation,spaces (clean the string)
lowercase the string
keep the digits(do not get rid of numbers)

E:

A:
iterate over all chars in the arg string
if char is alphanumeric, add to the char list
iterate again and lowercase uppercase chars (?)

calculate
{'m': 1, 'i': 4, 's': 4, 'p': 2}
{'a': 1, 'b': 1, 'c': 1, '1': 1, '2': 1, '3': 1}

-initialize a dict 
-iterate over values
-if the value is not a key in the dictionary, make it a key
-the value for that key will be in a list and will be the key from the original key (that Im iterating over)
-if the value already exists in the dictionary as a key, add the key into the list

user sort and sort in the reverse way

"""
def get_char_count(s):
    char_list= []

    for char in s:
        if char.isalnum():
            char_list.append(char.lower())
    # print(char_list)

    counted = {}
    for char in char_list:
        counted[char] = counted.get(char, 0) + 1
    # print(counted) #{'m': 1, 'i': 4, 's': 4, 'p': 2}

    result = {}
    for key, value in counted.items():
        if value not in result.keys():
            result[value] = [key]
        else:
            result[value].append(key)
            result[value].sort() # sorting the values

    sorted_result = dict(sorted(result.items(), reverse=True))

    print(sorted_result)

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

print('-----refactored but do not use: O2 complexity, solution down-----')
print('-----also incorrect because values should be sorted alphabetically-----')
def get_char_count(s):
    # char_list= []

    # for char in s:
    #     if char.isalnum():
    #         char_list.append(char.lower())
    char_list = [char.lower() for char in s if char.isalnum()]

    # print(char_list)

    # counted = {}
    # for char in char_list:
    #     counted[char] = counted.get(char, 0) + 1
    counted = {char: char_list.count(char) for char in char_list}

    # print(counted) #{'m': 1, 'i': 4, 's': 4, 'p': 2}

    # result = {}
    # for key, value in counted.items():
    #     if value not in result.keys():
    #         result[value] = [key]
    #     else:
    #         result[value].append(key)

    result = {}
    for key, value in counted.items():
        result[value] = result.get(value, []) + [key]
        # print('building result')
        # print(result)

    # sorted_result = dict(sorted(result.items(), reverse=True))
    # print(sorted_result)
    print(dict(sorted(result.items(), reverse=True)))

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

print('---Kelley, incorrect')
def get_char_count(input_string):
    chars = [char for char in input_string.lower() if char.isalnum()]
    counts = {}
    final = {}
    sorted_final = {}
    for char in chars:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count in final:
            final[count].append(char)    #How to append a list as a dictionary value.
        else:
            final[count] = [char]
    for count in final:
        final[count].sort(reverse=True)
    for count in sorted(final.keys(), reverse=True):
        sorted_final[count] = final[count]

    print(sorted_final)

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

print('---Kelley -another version, correct:')

def get_char_count(string):
    counts = {}
    for char in [char for char in string.lower() if char.isalnum()]:
        counts[char] = counts.get(char, 0) +1

    final = {}
    for key, value in counts.items():
        if value in final:
            final[value].append(key)
        else:
            final[value] = [key]

    sorted_final = {}
    sorting_keys = sorted(final.keys(), reverse= True)

    for value in sorting_keys:
        sorted_final[value] = sorted(final[value], reverse=False)

    print(sorted_final)
    return sorted_final

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}


print('---refactored but do not use due to O2 complexity')
def get_char_count(s):
    char_list = [char.lower() for char in s if char.isalnum()]

    counted = {char: char_list.count(char) for char in char_list} # O2 complexity too high!!!

    result = {}
    for key, value in counted.items():
        result[value] = result.get(value, []) + [key]

    print(dict(sorted(result.items(), reverse=True)))

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

print('fixed the O2 complexity - Gemini advice')
def get_char_count(s):
    # 1. Clean the string
    char_list = [char.lower() for char in s if char.isalnum()]

    # 2. Count efficiently (O(n) instead of O(n^2))
    counted = {}
    for char in char_list:
        counted[char] = counted.get(char, 0) + 1

    # 3. Group by frequency
    result = {}
    for char, freq in counted.items():
        # Using .append() is more efficient than [] + [key]
        if freq not in result:
            result[freq] = []
        result[freq].append(char)
        # Sort internally if you want alphabetical order
        result[freq].sort()

    # 4. Final sort of the dictionary by frequency
    sorted_result = dict(sorted(result.items(), reverse=True))

    print(sorted_result)
    return sorted_result
get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

print('Gemini solution')
import collections

def get_char_count(s):
    # 1. Clean and Count
    counts = collections.Counter(c.lower() for c in s if c.isalnum())
    # print(counts) #Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

    # 2. Group characters by their frequency
    groups = collections.defaultdict(list)
    for char, freq in counts.items():
        groups[freq].append(char)
    # print(groups) #defaultdict(<class 'list'>, {1: ['m'], 4: ['i', 's'], 2: ['p']})

    # 3. Sort keys descending AND internal lists alphabetically
    # FIX: We iterate through the sorted keys and grab the list from 'groups'
    result = {
        freq: sorted(groups[freq])
        for freq in sorted(groups.keys(), reverse=True)
    }
    # 3. Sort ONLY the keys (frequencies) descending
    # We take the list exactly as it was built in step 2
    # result = {
    #     freq: groups[freq] # no sort if we don't need the letters to be alphabetically in order
    #     for freq in sorted(groups.keys(), reverse=True)
    # }

    print(result)
    return result

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}