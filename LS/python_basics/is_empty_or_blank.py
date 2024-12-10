# Write an is_empty_or_blank function to determine
# whether a string is either empty or consists entirely of spaces. For example:

def is_empty_or_blank(string):
    return string.strip() == '' or string.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

print()
def is_empty_or_blank(string):
        return string.strip(' ') == ''

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

print()


def is_empty_or_blank(string):
    return len(string.strip(' ')) == 0


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))  # True
print(is_empty_or_blank(''))  # True