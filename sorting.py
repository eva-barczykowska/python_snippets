cities = ["Austin", "Spokane", "Durham", "Chicago"]
sorted_cities = sorted(cities) # sorted returns a NEW LIST
print(sorted_cities) # ['Austin', 'Chicago', 'Durham', 'Spokane']
print(cities) # ['Austin', 'Spokane', 'Durham', 'Chicago']

# Lists also have a sort method, but that sorts lists in-place and it only works on lists:

tools = ["pytest", "Ruff", "tox", "Mypy"]
tools.sort()  # sorts IN-PLACE!, mutating!
print(tools) # ['Mypy', 'Ruff', 'pytest', 'tox'] #sorted differently coz of capitalization

# we can have a solution for this

# We can fix that by passing a key function to sorted:

tools = ["pytest", "Ruff", "tox", "Mypy"]
sorted_tools = sorted(tools, key=str.casefold)
print(sorted_tools) # ['Mypy', 'pytest', 'Ruff', 'tox']
tools = ["pytest", "Ruff", "tox", "Mypy"]
sorted_tools = sorted(tools, key=str.upper) # we are not using () when we pass a function AS AN ARGUMENT
print(sorted_tools) # ['Mypy', 'pytest', 'Ruff', 'tox']


