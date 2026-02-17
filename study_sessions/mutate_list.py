# # Sum of Sums
# # Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

# """
# problem: sum up not as a total sum but against a counting Sum
# input: list of numbers
# output: integer

# example:
# first round sum is 3 = 3
# secound round sum is 3 +5 = 8
# third round sum is 10  = 3 + 8 + 11

# data structure, list

# algorithm:

# initiate a total counter at zero
# initiate a running counter? at zero?
# iterate over list
#  add number to running counter
#  add running to total?


# """

# def sum_of_sums(lst):
#     counter = 0
#     running = 0
#     for item in lst:
#         running += item
#         counter += running

#     print(counter)
#     return counter


# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

''' Sum of Digits
# Write a function that takes one argument, a positive integer, and returns the sum of its digits

P:
-func takes 1 arg, a positive integer
-func returns sum of its digits

#E:

A:
-cast to str
-split to have digits strings, this is a list
-map/transform these digits strings into numbers
-add numbers in the list
'''
# def sum_digits(digit):
#     str_digit = str(digit)
#     lst = []
#     for char in str_digit:
#         lst.append(char)

#     sum = 0
#     for a_num in lst:
#         sum += int(a_num)

#     return sum


# print(sum_digits(23) == 5)              # True
# # 2+3
# print(sum_digits(496) == 19)            # True
# # # 4+9+6 = 19
# print(sum_digits(123456789) == 45)      # True

# digits = [int(num) for num in str(integer)]

'''Staggered Case (Part 1)
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

iterate over the string
initiate a new string
every even index should be converted to upper()
every odd should be be added as is
ignore non alpha and just add as is

 'I Love Launch School!'
 "I LoVe lAuNcH ScHoOl!"
  0 2 4 6 7 8 

'''




# def staggered_case(string):
#     new_string = ""
#     for i in range(len(string)):
#         if string[i].isalpha() and i %2 == 0:
#             new_string += string[i].upper()
#         else:
#             new_string += string[i].lower()

#     return new_string

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

#Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order. You may assume that the argument will always be a positive integer.

# P:
# func takes an int , positive
# func returns a list of integers from 1 to that number inclusive

# E:
# A:
# -init a list result
# -go over the range, take + 1 because the range is not inclusive
# -append all these numbers from the range to the result


# def sequence(num):
#     # result = []
#     # for a_num in range(1, num+1):
#     #     result.append(a_num)

#     # return result

#     return [a_num for a_num in range(1, num+1)]

# print(sequence(5))# == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

'''Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument. You may not use the list.reverse method nor may you use a slice ([::-1]).

#[1, 2, 3, 4] index 0 becomes index - 1, index 1 becomes index -2
#[4, 3, 2, 1] index 2 becomes index -3? index 3 becomes index -4

P:
-func takes a list as an arg
-func reverses list elements IN PLACE
-the returned object shoud be THE SAME object used as an arg
-do not use list.reverse or a slice, [::-1]
-so how else mutate it???



A:
-I could use list.sort() NO, this won't work

l[index]=
get indexes from last to first
put last element first,second last second, third last third, etc.
'''

def reverse_list(lst):
    first = 0
    last = -1
    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    return lst

def reverse_list(lst):
    n = len(lst)
    for index in range(n//2):
        lst[index], lst[-(index + 1)] = lst[-(index + 1)],  lst[index]
    return lst





list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True