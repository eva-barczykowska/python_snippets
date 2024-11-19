# You will be given an array of numbers. You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
#
# [7, 1] = > [1, 7]
# [5, 8, 6, 3, 4] = > [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = > [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# -odd need to be sorted in ascending order
# -even stay the same
# we extract odd numbers from the array and sort them
# iterate over the input lst
# initialize counter to 0
# if a number is odd, take it from the odd_numbers using the counter
#     increase the counter by 1
#     else just copy it from the original list
#
# return result

def sort_array(arr):
    result = []
    odd_numbers = sorted([num for num in arr if num % 2 != 0])
    counter = 0

    for num in arr:
        if num % 2 != 0:
            result.append(odd_numbers[counter])
            counter += 1
        else:
            result.append(num)

    return result


# print(sort_array([5, 3, 2, 8, 1, 4]))  #, [1, 3, 2, 8, 5, 4])
# print(sort_array([5, 3, 1, 8, 0]))  #, [1, 3, 5, 8, 0])
# print(sort_array([]))  #, [])
print(sort_array([5, 3, 2, 8, 1, 4, 11]))  #, [1, 3, 2, 8, 5, 4, 11])
# print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]))  #, [2, 22, 1, 5, 4, 11, 37, 0])
# print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))  #, [1, 1, 5, 11, 2, 11, 111, 0])

print()


def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]  # very nice!


print(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0])
print(sort_array([]) == [])
print(sort_array([5, 3, 2, 8, 1, 4, 11]) == [1, 3, 2, 8, 5, 4, 11])
print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]) == [2, 22, 1, 5, 4, 11, 37, 0])
print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]) == [1, 1, 5, 11, 2, 11, 111, 0])
