# Define a function postalValidate(S) which first checks if S represents a postal code which is valid:
# first, delete all spaces;
# the remainder must be of the form L#L#L# where L are letters (in either lower or upper case) and # are numbers.
# If S is not a valid postal code, return the boolean False. If S is valid, return a version of the same postal code
# in the nice format L#L#L# where each L is capital.

# Algorithm:
# - remove all spaces from the input string
# - check if the resulting string is of length 6
# if not, return False

# - check if the string matches the L#L#L# pattern
# if not, return False

# create a range of 6 integer
# iterate over the range and use indices(numbers of the range) to check
# if a character at the given index if evenly divisible by 2
# if it is not, it means it's a number and then we need to check if that character isalpha()
# if not return false
# else check the characters at indices that are odd
# use and isdigit() to check if each of those characters is a number
# if it is not a number, return False

# finally return the postal code in uppercase

def postal_validate(s):
    s = s.replace(" ", "")

    # Check if the length is exactly 6
    if len(s) != 6:
        return False

    # Check if the string matches the L#L#L# pattern
    for i in range(6):
        if i % 2 == 0:  # Expecting a letter at these positions
            if not s[i].isalpha():
                return False
        else:  # Expecting a number at these positions
            if not s[i].isdigit():
                return False

    # If all checks pass, return the formatted postal code
    return s.upper()


def postal_validate(s):
    s = s.replace(" ", "")

    if len(s) != 6:
        return False

    # Step 3: Check character by character
    # L#L#L# -> 0, 2, 4 should be letters; 1, 3, 5 should be numbers
    if s[0].isalpha() and s[1].isdigit() and s[2].isalpha() and s[3].isdigit() and s[4].isalpha() and s[5].isdigit():
        # Step 4: Return the formatted string in uppercase
        return s.upper()

    # If any check fails, return False
    return False


# Example usage
print(postal_validate("K1A 0B1"))  # Output: 'K1A0B1'
print(postal_validate("A1B 2C3"))  # Output: 'A1B2C3'
print(postal_validate("123 ABC"))  # Output: False
