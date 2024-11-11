#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29  # calculate the sum of odd numbers in each row

"""
Sure, let’s go over the problem step by step in simpler terms.

### Problem Breakdown
You’re given a triangle of consecutive odd numbers, and each row has more numbers than the previous row.
Here’s the pattern:

1. Row 1: `1`  → sum is `1`
2. Row 2: `3, 5`  → sum is `8`
3. Row 3: `7, 9, 11`  → sum is `27`
4. Row 4: `13, 15, 17, 19`  → sum is `64`

### Goal
The task is to find the sum of the numbers in any row ( n ) without having to add each number manually.

### Key Insight
The sum of the numbers in row ( n ) can be found using a simple mathematical formula:
[text{Sum of row } n = n^3]

This means that for:
- Row 1, the sum is (1^3 = 1)
- Row 2, the sum is (2^3 = 8)
- Row 3, the sum is (3^3 = 27)
- Row 4, the sum is (4^3 = 64)

This pattern holds for every row in the triangle.

### Why This Works
Each row ( n ) in the triangle has exactly ( n ) odd numbers, and as we go down each row,
the numbers continue sequentially from where the last row left off. This pattern is specific
to odd numbers in this triangle structure, and the formula ( n^3 ) gives the correct sum
without needing to add each individual number.

### Solution in Code

Here’s the Python function to calculate the sum for any row ( n ):

```python
def row_sum_odd_numbers(n):
    return n ** 3
```

### Explanation of the Code
This function simply returns ( n^3 ), which is the sum of the numbers in the ( n )-th row.

### Example Calculations
- For ( n = 1 ): `1 ** 3 = 1`
- For ( n = 2 ): `2 ** 3 = 8`
- For ( n = 3 ): `3 ** 3 = 27`
- For ( n = 4 ): `4 ** 3 = 64`

Each result matches the sum of the numbers in the corresponding row of the triangle.
"""


def row_sum_odd_numbers(n):
    return n ** 3


# print(row_sum_odd_numbers(1)  #1)
print(row_sum_odd_numbers(2))  # 8)
# print(row_sum_odd_numbers(13), 2197)
# print(row_sum_odd_numbers(19), 6859)
# print(row_sum_odd_numbers(41), 68921)
