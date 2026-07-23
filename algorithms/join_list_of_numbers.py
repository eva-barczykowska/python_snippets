numbers = [1, 2, 3, 4, 5]

joined = "".join(map(str, numbers))
print(joined)

joined2 = "".join(str(n) for n in numbers)
print(joined2)

# "".join(numbers) # will not work as expected, as it tries to convert the list to a string

# generator expression that iterates over the `numbers` iterable

# A generator expression (`str(n) for n in numbers`) avoids creating an intermediate list of strings,
# making it more memory-efficient.

# If you used a list comprehension instead (`str(n) for n in numbers`), it would create an intermediate list before joining,
# which can be less efficient for large datasets.