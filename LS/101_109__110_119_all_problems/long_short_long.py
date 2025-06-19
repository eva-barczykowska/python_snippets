# Short Long Short
# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# These examples should all print True

def short_long_short(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 < len2:
        new_string = string1 + string2 + string1
        return new_string
    elif len1 > len2:
        new_string = string2 + string1 + string2
        return new_string


print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")