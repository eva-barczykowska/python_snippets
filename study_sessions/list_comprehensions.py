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