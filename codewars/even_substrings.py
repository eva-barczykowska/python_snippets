"""

Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

problem: coerce string to a number, evaluate if the number is even, if so hold it and return the total number of even splits.

input: string of digits
output: integer, number of even strings

example:  1432:
1
14 EVEN
143
1432 EVEN
4 EVEN
43
432 EVEN
3
32 EVEN
2 EVEN

Data structure = list for holding

algorithm:

- nested for loop over the string, make the slices, append to a holding list

- iterate over the holding list,
    - convert each number to an integer
    - do the even modulo, and if yes, apend to second holding list

    return len second holding list

STRING: '1432'
i: 0, j: 1, [0:1] substring: 1
i: 0, j: 2, [0:2]  substring: 14
i: 0, j: 3, [0:3] substring: 143
i: 0, j: 4, [0:4] substring: 1432
i: 1, j: 2, [1:2]substring: 4
i: 1, j: 3, [1:3] substring: 43
i: 1, j: 4, [1:4] substring: 432
i: 2, j: 3, [2:3] substring: 3
i: 2, j: 4, [2:4] substring: 32
i: 3, j: 4, [3:4] substring: 2
"""
def even_substrings(str_number):
    result = []

    # We only need one nested loop to find all possible substrings
    for i in range(len(str_number)):
        # j starts from i+1 to ensure we get at least one character
        for j in range(i + 1, len(str_number) + 1): # [0:1], [0:2], [0:3],[0:4] * [1:2], [1:3], [1:4] * [2:3], [2:4], [3:4]
            # print(f'i: {i}, j: {j}, substring: {str_number[i:j]}')
            substring = str_number[i:j]

            # Convert to int and check if even
            if int(substring) % 2 == 0:
                result.append(int(substring))

    return len(result)

print(even_substrings('1432') == 6)       # True
print(even_substrings('3145926') == 16)   # True
print(even_substrings('2718281') == 16)   # True
print(even_substrings('13579') == 0)      # True
print(even_substrings('143232') == 12)    # True

print('---')
# AI suggested solution/logic
# The Logic: An integer is even if and only if its last digit is even.In '1432', any substring ending in '4' or '2' is
# even.Substrings ending in '4': 14, 4 (2 total)Substrings ending in '2': 1432, 432, 32, 2 (4 total)Total: $2 + 4 = 6$.

# This is O(n) instead of O(2)

def even_substrings(str_num):
    total = 0
    for indx, digit in enumerate(str_num): #'1432' digit is 0, 1, 2, 3
        # print(f'i: {i}, digit: {digit}')
        # i: 0, digit: 1
        # i: 1, digit: 4 # at this point it's 1(index) + 1 = 2 so total is 2
        # i: 2, digit: 3
        # i: 3, digit: 2  # at this point it's
        # 3(index) + 1 = 4 so total is 4, that's our new total, we disregard the previous total
        if int(digit) % 2 == 0:
            # If the digit at index i is even,
            # all substrings starting before it and ending at it are even.
            total += (indx + 1)
    return total

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

