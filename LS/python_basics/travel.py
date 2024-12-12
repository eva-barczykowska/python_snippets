destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# Write a function that, without using the built-in in operator, checks whether a specific destination is included
# within destinations. For example: When checking whether 'Barcelona' is contained in destinations,
# the expected output is True, whereas the expected output for 'Nashville' is False.

def contains(target_destination, destinations):
    counter = 0
    while counter < len(destinations):
        if destinations[counter] == target_destination:
            return True
        else:
            counter += 1
            continue
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

# ls solution, with for loop


def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False


# def contains(destination, destinations):
#     return destination in destinations
#
# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False