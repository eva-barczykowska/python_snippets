# Implement the function unique_in_order which takes as argument a sequence and returns
# a list of items without any elements with the same value next to each other and preserving
# the original order of elements.
#
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# PEDAC
# -if it's false (coz it's empty), return an empty list
# -else get indices
# -iterate over indices and append the current element to the result list
# if it's not the same as the previous one
#
# -return the result list


def unique_in_order(seq):
    if not seq:
        return []

    indices = list(range(len(seq)))
    result = []

    for i in indices:
        if i == 0 or seq[i] != seq[i - 1]:
            result.append(seq[i])

    return result


print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3])

from itertools import groupby


# Using itertools.groupby to group consecutive identical elements in the sequence,
# and then converting the resulting groups into a list of tuples where each tuple contains
# a unique element and its count.
def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]


print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3])

print()

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3])


def unique_in_order(iterable):
    return [ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1]]


print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3])


# -initialize an empty list, k
# - iterate over the iterable using the for loop
#     - if k is empty, append the current element to k
#     - else, check if the current element is the same as the last element in k
#         - if they are not the same, append the current element to k

# return k

def unique_in_order(iterable):
    k = []
    for i in iterable:  # iterate over the iterable
        if not k:  # if k is empty, this will work for the first element
            k.append(i)
        elif k[-1] != i:  # this will work for the rest of the elements
            k.append(i)
    return k


print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
print(unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3])
print(unique_in_order(''))  # == []
print(unique_in_order([]))  # == []
