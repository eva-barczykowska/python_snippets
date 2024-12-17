# Create a dictionary that contains the following data, and assign it to a variable named car.
#
# type	color	mileage
# sedan	blue	80000

my_car = {'type': 'fiat', 'color': 'turquoise', 'mileage': 80000}
his_car = {'type': 'fiat', 'color': 'red', 'mileage': 120000}
# print(my_car)

# HASHABLE_TYPES = (int, float, str, tuple, frozenset)

# In addition to immutability, dictionary keys must also be hashable.
# A hashable type is a type from which consistent hash values can be computed.

# A hash function is used to compute hash value of an object.
# It takes the object and returns a hash value,
# which is used internally in a dictionary to store and retrieve values.
#
# Given two identical objects, the hash function must return the same value for both objects.

print(hash(my_car['type']) == hash(his_car['type']))  # True    )

# Tuples can be used as dictionary keys since they are immutable.
# However, this only applies if all the elements inside the tuple are also immutable and hashable.
# For example, a tuple that contains lists cannot be used as a dictionary key since lists are mutable and non-hashable,
# making the entire tuple non-hashable as well.
