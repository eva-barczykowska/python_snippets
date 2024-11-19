def pipe_fix(nums):
    ordered = sorted(nums)
    return list(range(ordered[0], ordered[-1] + 1))


print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(pipe_fix([1, 2, 3, 12]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(pipe_fix([6, 9]))  # , [6, 7, 8, 9])
print(pipe_fix([-1, 4]))  # , [-1, 0, 1, 2, 3, 4])
print(pipe_fix([1, 2, 3]))  # , [1, 2, 3])

print()


def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))


print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(pipe_fix([1, 2, 3, 12]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(pipe_fix([6, 9]))  # , [6, 7, 8, 9])
print(pipe_fix([-1, 4]))  # , [-1, 0, 1, 2, 3, 4])
print(pipe_fix([1, 2, 3]))  # , [1, 2, 3])

print()


def pipe_fix(l):
    return [x for x in range(min(l), max(l)+1)]

print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(pipe_fix([1, 2, 3, 12]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(pipe_fix([6, 9]))  # , [6, 7, 8, 9])
print(pipe_fix([-1, 4]))  # , [-1, 0, 1, 2, 3, 4])
print(pipe_fix([1, 2, 3]))  # , [1, 2, 3])

print()


def pipe_fix(arr):
    ls = []
    for i in range(arr[0],arr[len(arr)-1]+1):
        ls.append(i)
    return ls


print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(pipe_fix([1, 2, 3, 12]))  # , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(pipe_fix([6, 9]))  # , [6, 7, 8, 9])
print(pipe_fix([-1, 4]))  # , [-1, 0, 1, 2, 3, 4])
print(pipe_fix([1, 2, 3]))  # , [1, 2, 3])