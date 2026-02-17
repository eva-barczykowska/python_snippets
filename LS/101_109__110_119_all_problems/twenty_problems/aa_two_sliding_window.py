# Create a function that takes a list of integers as an argument. The function should return
# the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should
# return None.
# P:
# -function takes a list of integers as an argument
# -function returns the minimum sum of 5 consecutive numbers in the list
# -if the function contains fewer than 5 elements, the function should return None

# A:
# Step 1: Handle the edge case where the list is too short.
# Step 2: Calculate the sum of the first window of 5 elements.
# This will be our initial minimum sum to beat.
# Step 3: Slide the window across the rest of the list.
# We start from the 6th element (index 5) and go to the end.
# Step 4: Update the minimum sum if a smaller sum is found.
# Step 5: Return the minimum sum found.

def minimum_sum(num_list):
    if len(num_list) < 5:
        return None

    current_sum = sum(num_list[0:5])
    min_so_far = current_sum

    for index in range(5, len(num_list)): # starting from index 5, which is element 6 since indexes start from 0.
        # This is the efficient part: instead of re-calculating the whole sum,
        # we update the previous sum by adding the new element (num_list[i])
        # and subtracting the element that just fell out of the window (num_list[i-5]).
        current_sum = current_sum + num_list[index] - num_list[index - 5]
        # if we consider [1, 2, 3, 4, 5, -5], the element leaving the window is 1
        # the element coming in is -5,
        # so we subtract 1 from the current_sum (leaving element).
        # the sum of the new window is 9.



        # Check if this new window's sum is the smallest we've seen.
        if current_sum < min_so_far:
            min_so_far = current_sum

    # Step 4: Return the final minimum value found.
    return min_so_far



print(minimum_sum([1, 2, 3, 4]) is None) #True
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9) #True
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15) #True
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16) #True
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10) #True



# [55, 2, 6, 5, 1]
#      [2, 6, 5, 1, 2]
#         [6, 5, 1, 2, 9]
#            [5, 1, 2, 9, 3]
#               [1, 2, 9, 3, 5]
#                  [2, 9, 3, 5, 100]