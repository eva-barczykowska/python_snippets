'''
11:15
https://github.com/atropos-null/LS/blob/main/py119/the_twenty.md
Problem 1
Create a function that takes a list of numbers as an argument. For each number,
determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list,
it should only be counted once.

P:
function takes a list of numbers as an argument
for each number, find out HOW MANY numbers are smaller than this number
but the counting is unique, ie if we have twice number 2, it is counted only once
--how to do this bit?
--take all the other numbers than the current number
--make a set so you have only unique numbers to analyze
--analyze these numbers as above
--count the number of numbers which are smaller than the current number
place the answer in the list at the index of the number that is considered right now

E:
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]) #True
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]) #True
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]) #True
print(smaller_numbers_than_current([1]) == [0]) #True

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result) #True

A:
-take the arg
-iterate over the list of nums
--for each num
--save it to a variable `target`
--make a set from the rest of nums
--iterate use this unique set for counting how many numbers are smaller
--insert the result of counting into the `counted` list
'''

def get_all_other_numbers(list_of_numbers, index):
    copied = list_of_numbers.copy()
    copied.remove(list_of_numbers[index])
    return copied

# get_all_other_numbers([8, 1, 2, 2, 3], 0)



def smaller_numbers_than_current(list_of_numbers):
    result = []
    for index, num, in enumerate(list_of_numbers):
        target = list_of_numbers[index]
        all_other_nums = get_all_other_numbers(list_of_numbers, index)
        unique = list(set(all_other_nums))
        count = 0
        for unique_number in unique:
            if unique_number < target:
                count += 1
        result.append(count)
    return result


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))# == [3, 0, 1, 1, 2]) #True
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]) #True
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]) #True
print(smaller_numbers_than_current([1]) == [0]) #True

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result) #True

# error -why -Medium

# def smaller_numbers_than_current(list_of_numbers):
#     result = []
#     for index, num, in enumerate(list_of_numbers):
#         target = list_of_numbers[index]
#         all_other_nums = get_all_other_numbers(list_of_numbers, index)
#         unique = list(set(all_other_nums))
#         count = 0
#         for unique_number in unique:
#             if unique_number < target:
#                 count += 1
#         result.append(count)
#         return result # why returns [3] indentation, it is calculated result for after the finished first iteration of the [8, 1, 2, 2, 3], so this is at the point when it finished processing 8


print(('------- Improved version ---'))
def smaller_numbers_than_current_improved(numbers):
    # 1. Get the unique numbers from the input list and sort them.
    # This is the most expensive operation, but we only do it ONCE.
    # Complexity: O(n log n) for the sort.
    unique_sorted_nums = sorted(list(set(numbers))) #Once you have the sorted list of unique numbers, a number's position (or index) in that list is exactly the count of how many unique numbers are smaller than it.
    # print(unique_sorted_nums)

    # 2. Use a list comprehension to build the result.
    # This is more concise and often faster than a for-loop with .append().
    # For each number in the original list, its count of smaller unique numbers
    # is simply its index in the `unique_sorted_nums` list.
    # unique_sorted_nums is a list so we can use the index() method.
    # lets way we have [1, 2, 3, 8]
    # numbers is [8, 1, 2, 2, 3]
    # so for 8, index in unique_sorted_nums is 3, and it is indeed 3 numbers smaller than 8.
    # so for 8 we will return 3, which is the 8's index in the sorted list.
    return [unique_sorted_nums.index(num) for num in numbers]
# --- Let's test it ---
print(smaller_numbers_than_current_improved([8, 1, 2, 2, 3]))
# Expected: [3, 0, 1, 1, 2]
# How it works for [8, 1, 2, 2, 3]:
# unique_sorted_nums becomes [1, 2, 3, 8]
# For 8: index is 3
# For 1: index is 0
# For 2: index is 1
# For 2: index is 1
# For 3: index is 2
# Result: [3, 0, 1, 1, 2]
#
# def smaller_numbers_than_current_improved(numbers):
#     unique_sorted_nums = sorted(list(set(numbers)))
#     return [unique_sorted_nums.index(num) for num in numbers]

print('------- Performance test ---')
import timeit

def smaller_numbers_than_current(list_of_numbers):
    def get_all_other_numbers(lst, idx):
        return lst[:idx] + lst[idx+1:]

    result = []
    for index, num in enumerate(list_of_numbers):
        target = list_of_numbers[index]
        all_other_nums = get_all_other_numbers(list_of_numbers, index)
        unique = list(set(all_other_nums))
        count = 0
        for unique_number in unique:
            if unique_number < target:
                count += 1
        result.append(count)
    return result


def smaller_numbers_than_current_improved(numbers):
    unique_sorted_nums = sorted(list(set(numbers)))
    return [unique_sorted_nums.index(num) for num in numbers]


# test data
data = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(data))
print(smaller_numbers_than_current_improved(data))

# performance test
setup_code = """
from __main__ import smaller_numbers_than_current, smaller_numbers_than_current_improved
import random
data = [random.randint(0, 1000) for _ in range(1000)]
"""

time_old = timeit.timeit("smaller_numbers_than_current(data)", setup=setup_code, number=100)
time_new = timeit.timeit("smaller_numbers_than_current_improved(data)", setup=setup_code, number=100)

print(f"Old function time: {time_old:.4f} seconds")
print(f"Improved function time: {time_new:.4f} seconds")