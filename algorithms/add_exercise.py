# https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/?level=mixed

# I'd like you to write a function that accepts two lists-of-lists of numbers and returns
# one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

def add(matrix1, matrix2):
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [] # initializing an empty list for the result row
        for num1, num2 in zip(row1, row2):  # iterating over corresponding numbers in the rows
            result_row.append(num1 + num2)  # appending the sum of numbers to the result row
        result.append(result_row)
        # appending the result row to the result list
    return result


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2) == [[3, -3], [-3, 3]])

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]])

def add_optimized(matrix1, matrix2):
    return [[sum(pair) for pair in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2) == [[3, -3], [-3, 3]])

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]])