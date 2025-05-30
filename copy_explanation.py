import copy

# Original list with a nested list (a compound object)
original_list = [1, [10, 20], 3]

# Perform a shallow copy
shallow_copied_list = copy.copy(original_list)
# Alternatively, for lists, you can use:
# shallow_copied_list = original_list.copy() # so copy() or import copy and then use copy.copy()
# shallow_copied_list = original_list[:]

print(f"Original list: {original_list}")
print(f"Shallow copied list: {shallow_copied_list}")

print()
# Let's verify that the outer lists are different objects
print(f"Original list ID: {id(original_list)}")
print(f"Shallow copied list ID: {id(shallow_copied_list)}")
print(f"Are outer lists the same object? {original_list is shallow_copied_list}") # False

# Now, let's verify that the *inner nested lists* are the same object
print(f"Original inner list ID: {id(original_list[1])}")
print(f"Shallow copied inner list ID: {id(shallow_copied_list[1])}")
print(f"Are inner lists the same object? {original_list[1] is shallow_copied_list[1]}") # True

# Now, modify the inner list using the shallow_copied_list
shallow_copied_list[1].append(30)

print(f"\nAfter modifying inner list via shallow copy:")
print(f"Original list: {original_list}")             # Change is reflected here
print(f"Shallow copied list: {shallow_copied_list}") # Change is reflected here

# Modify the inner list using the original_list
original_list[1].append(40)

print(f"\nAfter modifying inner list via original list:")
print(f"Original list: {original_list}")             # Change is reflected here
print(f"Shallow copied list: {shallow_copied_list}") # Change is reflected here

# whichever object we modify it FROM, i.e. from the original_list or the shallow_copied_list,
# the change will be reflected in both. That is if the original object is mutable (like a list).
# This is because Python passes objects by reference, not by value, which means means if we use the copy() function
# to create a shallow copy,
# so when we modify this mutable object from/in either the original object or from the copy of that original object
# we actually access the same place in memory: the mutable object(like a list) in the original list and copied list
#  share the same memory locations.
# so the list in the copy is actually the same list as the one in the original object.
# This is what is meant by saying it is a reference


# DEEP COPY
print("--------------------DEEP COPY-----------------")
import copy

# Original list with a nested list
original_list = [1, [10, 20], 3]

# Perform a deep copy
deep_copied_list = copy.deepcopy(original_list)

print(f"Original list: {original_list}")
print(f"Deep copied list: {deep_copied_list}")

# Verify that the outer lists are different objects
print(f"Original list ID: {id(original_list)}")
print(f"Deep copied list ID: {id(deep_copied_list)}")
print(f"Are outer lists the same object? {original_list is deep_copied_list}") # False

# Verify that the *inner nested lists* are also different objects
print(f"Original inner list ID: {id(original_list[1])}")
print(f"Deep copied inner list ID: {id(deep_copied_list[1])}")
print(f"Are inner lists the same object? {original_list[1] is deep_copied_list[1]}") # False (This is the key difference!)

# Now, modify the inner list using the deep_copied_list
deep_copied_list[1].append(30)

print(f"\nAfter modifying inner list via deep copy:")
print(f"Original list: {original_list}")             # NOT affected
print(f"Deep copied list: {deep_copied_list}") # Only the copy is affected

# Modify the inner list using the original_list
original_list[1].append(40)

print(f"\nAfter modifying inner list via original list:")
print(f"Original list: {original_list}")             # Only the original is affected
print(f"Deep copied list: {deep_copied_list}") # NOT affected
