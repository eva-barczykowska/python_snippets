# The snail crawls up the column. During the day it crawls up some distance.
# During the night she sleeps, so she slides down for some distance (less than crawls up during the day).
#
# Your function takes three arguments:
#
# The height of the column (meters)
# The distance that the snail crawls during the day (meters)
# The distance that the snail slides down during the night (meters)
# Calculate number of day when the snail will reach the top of the column.

# PEDAC
# in a day she can do day meters
# in the night we need to subtract night meters
# we need to calculate how many days it takes for the snail to reach the top of the column

# Examples
# print(snail(3, 2, 1))  #, 2)
# 1st day - 2 meters, we have 2 m at the end of the day
# night - 1 meter, now we have 1 m at the end of the night
# 2nd day 1 + 2 so column was reached at the end of the 2nd day --- 2 should be returned

# print(snail(10, 3, 1), 5)
# 1st day - 3 meters, we have 3 m at the end of the day
# night - 1 meter, now we have 2 m at the end of the night
# 2day - 2 + 3 = 5 m at the end of the 2nd day
# night - 1, we have 4
# 3rd day 4 + 3 = 7 m at the end of the 3rd day
# night - 1, we have 6
# 4th day 6 + 3 = 9 m at the end of the 4th day
# night - 1, we have 8
# 5th day 8 + 3 = 11 m at the end of the 5th day --- should return 5

# print(snail(10, 3, 2), 8)
# 1st day - 3 meters, we have 3 m at the end of the day
# night - 2 meters, now we have 1 m at the end of the night
# 2nd day 1m + 3m = 4 m at the end of the 2nd day
# night, 4-2 = 2
# 3rd day 2m + 3m = 5 m at the end of the 3rd day
# night 5-2 = 3
# 4th day 3m + 3m = 6 m at the end of the 4th day
# night 6-2 = 4
# 5th day 4m + 3m = 7 m at the end of the 5th day
# night 7-2 = 5
# 6th day 5m + 3m = 8 m at the end of the 6th day
# night 8-2 = 6
# 7th day 8m + 3m = 11 m at the end of the 7th day
# night 11-2 = 9
# 8th day 11m + 3m = 14 m at the end of the 8th day -- should return 8

# print(snail(5, 10, 3), 1)

# Algorithm:
# init `days_needed` to 0
# init `current_progress` to 0
# while current_progress is smaller than column_height
#     add 1 to `days_needed`
#     if current_progress is equal or greater than column_height
#     break from the loop and return `days_needed`
#     minus `night`
# return `days_needed`


def snail(column, day, night):
    days_needed = 0
    current_progress = 0

    while current_progress <= column:
        current_progress += day
        days_needed += 1
        if current_progress >= column:
            return days_needed
        else:
            current_progress -= night

    return days_needed


print(snail(3, 2, 1))  #, 2)
print(snail(10, 3, 1), 5)
print(snail(10, 3, 2), 8)
print(snail(5, 10, 3), 1)

print()
from math import ceil


def snail(column: int, up: int, down: int) -> int:
    return max(ceil((column - down) / (up - down)), 1)

print(snail(3, 2, 1))  #, 2)
print(snail(10, 3, 1), 5)
print(snail(10, 3, 2), 8)
print(snail(5, 10, 3), 1)
