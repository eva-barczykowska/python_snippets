# Using the following code, compare the value of name with the string 'RoGeR'
# while ignoring the case of both strings. Print true if the values are the same;
# print false if they aren't. Next, perform a case-insensitive comparison between
# the value of name and the string 'DAVE'.

# name = 'Roger'
# print(name.lower() == 'RoGeR'.lower())
# print(name.lower() == 'DAVE'.lower())

name = 'Roger'

print(name.casefold() == 'RoGeR'.casefold())      # True
print(name.casefold() == 'DAVE'.casefold())       # False

print()
# use casefold, it offers more comprehensive approach to case-insensitive comparison
string1 = "SS".lower()
string2 = "ß".lower()
print(string1 == string2)                         # False

string1_casefolded = "SS".casefold()
string2_casefolded = "ß".casefold()
print(string1_casefolded == string2_casefolded)   # True