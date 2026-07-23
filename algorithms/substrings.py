"""
Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer.

Examples:
solve("1341") # should return 7
solve("1357") # should return 10

Problem:
-take a string and create substrings gradually
-see what substrings, when converted to int, are odd numbers
-create them and count how many you have
-return that number

Examples
solve("1341") # should return 7

1341
----
1
13
134
1341
-3
-34
-341
--4
--41
---1

-> 10 substrings in total
-> 7 odd numbers: 1, 13, 1341, 3, 341, 41, 1
solve("1357") # should return 10

A:
-iterate over the string and gradually cut substrings
-outer loop and inner loop
-add the generated substrings to a list
-covert the strings in the list to nums
-count odd nums
-return the count
"""

def solve(s):
    substrings = []
    outer_counter = 0
    inner_counter = 1
    while outer_counter < len(s):
        while inner_counter < len(s) + 1:
            one_string = s[outer_counter:inner_counter]
            if one_string != "":
                substrings.append(one_string)
            inner_counter += 1
        outer_counter += 1
        inner_counter = 1
    nums = [int(s) for s in substrings if int(s) % 2]
    return len(nums)


print(solve("1341") == 7) # should return 7)
print(solve("1357") == 10) # should return 10

#AI feedback
# 1.	Too many variables: outer_counter, inner_counter, substrings — a bit more verbose than needed.
# 2.	Appending all substrings first and then filtering → uses extra memory.
# 3.	Using while loops where for loops would be more readable.

def solve(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if int(s[i:j]) % 2 == 1:
                count += 1
    return count

print(solve("1341") == 7) # should return 7)
print(solve("1357") == 10) # should return 10