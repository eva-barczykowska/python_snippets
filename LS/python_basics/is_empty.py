# Write a function that checks whether a string is empty or not. For example:
def is_empty(string):
    return not string


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

print()
def is_empty(string):
    return string == ''


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


print()
# OR

def is_empty(string):
    return len(string) == 0


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True