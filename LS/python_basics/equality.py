# Predict the output of the code shown below. When you run the code, do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

# == tests if the two lists have the same elements in the same order.

# In Python, when comparing two lists using the equality operator (==),
# the comparison is based on the values contained within the lists, not their identity (memory location).
# If the two lists contain the same values in the same order, the comparison will return True.
#
# However, since list1 and list2 are two distinct objects in memory, the is operator will return False:

print(list1 is list2)  # False
# The is operator checks for identity; that is, it checks whether two objects are the same object in memory: