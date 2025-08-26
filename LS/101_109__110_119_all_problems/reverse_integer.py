"""Write a function that takes a positive integer as an argument and returns that number with its digits reversed.
"""
# P:
# function takes positive int
# function returns that number with its digits reversed

# E:
# 1 stays the same
# zeros at the beginning get removed (startswith)

# A:
# -if 1 digits return as it is
# -change the int into a str
# -use slicing to invert it
# -check for 0 with (startswith)
# -change back into int!

def reverse_number(number):
    if len(str(number)) == 1: # don't even neeed this part, see below
        return number
    else:
        s = str(number)
        reversed = s[::-1]
        if not reversed.startswith('0'):
            return int(reversed)

    return int(reversed.lstrip('0'))


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True


def reverse_number(number):
    s = str(number)
    reversed = s[::-1]
    if not reversed.startswith('0'):
        return int(reversed)

    return int(reversed.lstrip('0'))


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True