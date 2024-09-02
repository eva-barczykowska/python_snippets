from collections import Counter

# things = ["apple", "banana", "apple", "orange", "banana", "grape"]
# counted_things = {}
#
# for item in things:
#     if item not in counted_things:
#         counted_things[item] = 0
#     counted_things[item] += 1
#
#     print(counted_things)  # this prints out the current state of the dictionary at each iteration

# things = ["apple", "banana", "apple", "orange", "banana", "grape"]
# counted_things = {}
#
# for item in things:
#     if item not in counted_things:
#         counted_things[item] = 0
#     counted_things[item] += 1
#
# print(counted_things)  # this prints out the current state of the dictionary AFTER the loop has finished

things = ["apple", "banana", "apple", "orange", "banana", "grape"]
counted_things = Counter(things)

print(counted_things)  # MOST PYTHONIC WAY: using the Counter class from the collections module
