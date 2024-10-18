# Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

for key in ['name', 'grade']:
    if key in student:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

# another solution

print('name' in student)      # False
print('grade' in student)     # True

# Similar to lists and strings, Python dictionaries also support the membership operator in.
# When used with a dictionary, it checks whether a specified key is present in the dictionary.
# If the key is found, the expression evaluates as True; otherwise, it evaluates as False.