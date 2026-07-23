# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.


def sum_mix(arr):
    list_sum = 0

    for element in arr:
        list_sum += int(element)

    return list_sum


print(sum_mix([9, 3, '7', '3']))  # , 22)
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # , 42)
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # , 41)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))  # , 45)
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))  # , 61)


def sum_mix(arr):
    return sum(map(int, arr))


print(sum_mix([9, 3, '7', '3']))  # , 22)
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # , 42)
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # , 41)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))  # , 45)
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))  # , 61)


def sum_mix(arr):
    return sum(int(n) for n in arr)


print(sum_mix([9, 3, '7', '3']))  # , 22)
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # , 42)
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # , 41)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))  # , 45)
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))  # , 61)


def sum_mix(arr):
    return sum(int(i) for i in arr)


print(sum_mix([9, 3, '7', '3']))  # , 22)
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # , 42)
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # , 41)
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))  # , 45)
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))  # , 61)
