mylist = [10, 30, 20]
sorted_list = sorted(mylist)
print(sorted_list)  # Output: [10, 20, 30]

mylist = [10, 30, 20]
mylist.sort() # sort() is mutating
print(mylist)  # Output: [10, 20, 30]


#what will not work?
# mylist = [10, 30, 20]
# sorted_list = mylist.sort()
print(sorted_list)  # Output: None - sort() returns None, not the sorted list

mylist = [10, 30, 20]
sorted_list = sorted(mylist, reverse=True)
print(sorted_list)  # Output: [30, 20, 10]

# Because the list is sorted in place, you have to be careful if more than one variable is pointing
# to the same place.

my_first_list = [11, 2, 3]
my_second_list = my_first_list
my_first_list.sort()
print(my_second_list) # Output: [2, 3, 11]


# Python 2 believes that integers are 'less' than strings
# mylist = ['5', 5, '3', 3, '10', 10, '0', 0]
# mylist.sort()
# print(mylist) # integers will come first, then strings but 10. will be before 3, coz strings are compared lexicographically

words = "It's a beautiful day"
words_list = words.split()
words_list.sort()
print(words_list) # Output: ['It', "'s", 'a', 'beautiful', 'day']
# Why is "It" the first word in our sorted list?  Because Python uses ASCII for its sorting, and capital letters come before lowercase ones.

mylist = [('c', 3), ('a', 1), ('b', 2)]
mylist.sort()
print(mylist) # Output: [('a', 1), ('b', 2), ('c', 3)]


my_list = [('a', 11000), ('b', 211), ('c', 3000)]
my_list.sort(key=lambda x: x[1])
print(my_list) # Output: [('b', 2), ('a', 1), ('c', 3)]

my_dict = {'a': 22, 'b': 1, 'c': 3}
# print(my_dict.items()) # Outputs: dict_items([('a', 22), ('b', 1), ('c', 3)])

for key, value in sorted(my_dict.items()): # sorted is getting tuples of key-value pairs
    print(key, value)

# for key, value in sorted(my_dict.items(), key=lambda item: item[1]):

# sort() sorts in place but works only on lists! It returns None.
# sorted() returns a new sorted list and it can be used with any iterable.
# my_str = "Hello World"
# my_str.sort()

# sorted can be passed a function
tools = ["pytest", "Ruff", "tox", "Mypy"]
sorted_tools = sorted(tools, key=str.casefold)
print(sorted_tools)

#look at line 63 and the use of str.casefold()
# This works because functions can be passed to other functions in Python.
#
# Also note that str.casefold is valid because methods are just functions attached to classes:
# str.casefold(some_string)
# is the same as some_string.casefold().

#if you need only n smallest or n largest elements, you can use heapq.nsmallest() or heapq.nlargest()
numbers = [7, 2, 5, 4, 7, 9, 3, 4]
from heapq import nsmallest
smallest_three_numbers = nsmallest(3, numbers)
print(smallest_three_numbers) #[2, 3, 4]

# if we want just 1 number we can use min(numbers) or max(numbers)

# how to find things efficiently in lists?
from bisect import bisect_left
cities = ["Austin", "Spokane", "San Diego", "Chicago"]
sorted_cities = sorted(cities)
print(sorted_cities) #['Austin', 'Chicago', 'San Diego', 'Spokane']
print(bisect_left(sorted_cities, "San Diego"))

print(sorted_cities[2])#'San Diego'
