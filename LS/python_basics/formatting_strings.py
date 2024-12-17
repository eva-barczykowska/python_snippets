name = "Victor"
profession = "programmer"

# How can you print the string Hello, Victor. You are a programmer. using the str.format method?
# You should fill in the name and profession in a string literal that contains the rest of the text.
# How can you achieve the same result using an f-string?


# Using str.format method:
print("Hello, {}. You are a {}.".format(name, profession))

# Using f-string:
print(f"Hello, {name}. You are a {profession}.")