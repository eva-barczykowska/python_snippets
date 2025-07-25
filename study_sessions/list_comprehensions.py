#Exercise 1: Basic List Comprehension
#Given a list of numbers, create a new list with each number doubled.

#Expected result:​ [2, 4, 6, 8, 10]

# numbers = [1, 2, 3, 4, 5]
# double_numbers = [number * 2 for number in numbers]
# print(double_numbers)


#Exercise 2: List Comprehension with Condition
#Given a list of numbers, create a new list containing only the even numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [num for num in numbers if num % 2 == 0]
# print(even)
#Expected result:​ [2, 4, 6, 8, 10]

#Exercise 3: String Transformation
#Given a list of words, create a new list with each word capitalized.

# words = ['hello', 'world', 'python', 'programming']
# caps = [word.capitalize() for word in words]
# print(caps)
#Expected result:​ ['Hello', 'World', 'Python', 'Programming']

#Exercise 4: Filtering with String Condition
#Given a list of words, create a new list containing only words that have more than 4 letters.
# words = ['cat', 'elephant', 'dog', 'giraffe', 'ant', 'zebra']
# four_letter_words = [word for word in words if len(word) >= 4]
# print(four_letter_words)
#Expected result:​ ['elephant', 'giraffe', 'zebra']

#Exercise 5: Working with Nested Lists
#Given a list of lists, create a new list containing the length of each sublist.

# lists = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
# lengths = [len(element) for element in lists ]
# print(lengths)

#Expected result:​ [2, 3, 1, 4]

#Exercise 6: Dictionary Values
#Given a dictionary, create a list of all the values.

# person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# # values = [person for person in person.items()]
# # print(values)
# #Expected result:​ ['Alice', 30, 'New York']

# values = [[person, data] for person, data in person.items()]
# # [['name', 'Alice'], ['age', 30], ['city', 'New York']]
# flattened = []
# for element in values:
#     flattened.extend(element)
# print(flattened)

#Exercise 7: Nested List Transformation
#Given a list of lists, create a new list containing the first element of each sublist.
lists = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]
#Expected result:​ ['a', 'd', 'f']

firsties = [element[0] for element in lists ]
print(firsties)

# join this list of int into a str

# numbers = [1, 2, 3, 4, 5]
# join_str = [''.join(str(num)) for num in numbers] #['1', '2', '3', '4', '5']
# print(join_str)

# join_str = '*'.join([str(num) for num in numbers]) # so put the join operation inside the list comprehension
# print(join_str)

# join_str = ''.join(str(num) for num in numbers) # this is GENERATOR EXPRESSION
# print(join_str)

# hex_numbers = [0xe1c5eb, 0x4bdc58, 0xc0f95e, 0xed22da, 0xabefe8, 0x20eb83]
# hex_sum = [sum(hex_numbers)]
# print(hex_sum)

#show the num of non-whitespace characters in the string
# string = "Hello World!"
# non_whitespace_count = sum([1 for char in string if char.isspace() == False])
# print(non_whitespace_count)

# now count whitespace characters
# string = "Hello World!"
# non_whitespace_count = sum([1 for char in string if char.isspace() == True])
# print(non_whitespace_count)

#or
string = "Hello World!"
non_whitespace_count = sum([1 for char in string if char == " "])
print(non_whitespace_count)

#Practice Problem 6 Transform the following list of tuples into a list of dictionaries with keys 'name' and 'score',
# but only include entries where the score is above 75.

#Expected result: [{'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 91}, {'name': 'Eve', 'score': 88}]

student_scores = [
    ('Alice', 85),
    ('Bob', 72),
    ('Charlie', 91),
    ('Diana', 68),
    ('Eve', 88)
]

# we have a list of tuples
# we want a list of dictionaries

# todict?

# immutable but we can iterate


my_dict = {}

l = []

for first, second, in student_scores:
    # temp = {}
    # temp[first] = second
    l.append({first: second})


# print(l)

list_comp = [{first: second} for first, second in student_scores ]
print(list_comp)


#Practice Problem 7
# Given the following dictionary, create a new dictionary where each key maps to a list of words from the original value that have more than 4 characters.

# Expected result: {'morning': ['quick', 'brown', 'jumps'], 'afternoon': ['sleeping'], 'evening': ['under', 'bright', 'starry']}

sentences = {
    'morning': 'the quick brown fox jumps',
    'afternoon': 'over the lazy dog sleeping',
    'evening': 'under the bright starry sky'
}

