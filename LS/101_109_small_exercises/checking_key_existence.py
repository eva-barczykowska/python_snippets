# Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

if 'name' in student:
    print("Both 'name' exists in the dictionary.")
elif 'grade' in student:
    print("The key 'grade' exists in the dictionary.")

# LS solution:
print('name' in student)      # False
print('grade' in student)     # True