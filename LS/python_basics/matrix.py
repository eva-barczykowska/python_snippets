# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game.
# However, we encountered an issue,
# as whenever we change a value in one nested list, all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    copied_sub_list = sub_list.copy()  # creating a deep copy of sub_list each time we append it to matrix
    matrix.append(copied_sub_list)  # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
