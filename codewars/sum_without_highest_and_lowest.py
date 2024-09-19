# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
# Input validation
# If an empty value ( None ) is given instead of an array,
# or the given array is an empty list or a list with only 1 element, return 0.
def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0

    sorted_lst = sorted(arr)

    sorted_lst.pop()
    sorted_lst.reverse()
    sorted_lst.pop()

    return sum(sorted_lst)


print(sum_array([6, 2, 1, 8, 10 ])) # should return 16
print(sum_array([1, 1, 11, 2, 3])) # should return 6