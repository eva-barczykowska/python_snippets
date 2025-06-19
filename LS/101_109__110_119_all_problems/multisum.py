#Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

#You may assume that the number passed in is an integer greater than 1.

# problem: sum the individual numbers before the number given, inclusive
# input = integer
# output = integer

#example: 20, outputs 98. Only numbers that are multiples of 3 and 5

#data structure: empty list

#algorithm
# 1) create empty list
# 2) for loop ... for i in range (1, i+1)
# 3) if i % 3 == 0, append list
# 4) if i % 5 == 0, append list
# 5) sum the list
#6) return the list


def multisum(num):
    multiples = []
    for i in range (1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)