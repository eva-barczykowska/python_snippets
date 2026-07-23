# https://www.pythonmorsels.com/pointers/?__s=a956w4b94d1g1dsg5whb&utm_source=drip&utm_medium=email&utm_campaign=Helpful+Python+resources&utm_content=Python%27s+variables+and+values+can+be+confusing

# Equality compares objects and identity compares pointers
my_numbers = [2, 1, 3, 4]
your_numbers = [2, 1, 3, 4]
print(my_numbers == your_numbers)  # Output: True

# Python's is operator checks whether two objects are the same object (a.k.a. identity):

print(my_numbers is your_numbers)  # Output: False
my_numbers.append(555)
print(my_numbers is your_numbers)  # Output: False
# appending to one list does not affect the other since they refer to different objects

my_numbers_again = my_numbers
print(my_numbers is my_numbers_again)  # Output: True

my_numbers_again.append(777)  # changes both variables because they refer to the same object
print(my_numbers)  # Output: [2, 1, 3, 4, 5]
print(my_numbers_again)  # Output: [2, 1, 3, 4, 5]

print(my_numbers is my_numbers_again)  # Output: True

# >>> n += 2
# >>> n = n + 2
# For immutable objects, augmented assignments (+=, *=, %=, etc.) perform an operation
# (which returns a new object) and then do an assignment (to that new object).