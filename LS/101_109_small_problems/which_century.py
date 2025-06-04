#What Century is That?
#Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

#New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

#Problem:
# - input: a 4 digit year
# - output: "20th" or "3rd"

#example = 2000 returns 20th

#data structure: None? Manipulating an integer and a returning a string?

#algorithim
# - integer always rounds up
# - a suffix to be affixed
# - match case to match the type
# reduce the century number to the stump, so if its a 2 digit number need a case for 2 digits, and a case for 1 digit
#
# 1st, 2nd, 3rd 4th, 5th
# if 1, goes up to 1st
#elif 2, becomes 2nd
#elif 3, becomes 3rd
#else:  th
#might need two functions, 1 to get the reduced number and the other to add the suffix


# def century(year):

#     century_num = year // 100 + 1
#     if year % 100 == 0:
#         century_num -= 1

#     suffix = century_suffix(century_num)
#     return f"{century_num}{suffix}"

# def century_suffix(century_num):

#     last_2digit = century_num % 100
#     last_digit = century_num % 10

#     match last_2digit:
#         case 11 | 12 | 13:
#             return 'th'

#     match last_digit:
#         case 1:
#             return 'st'
#         case 2:
#             return 'nd'
#         case 3:
#             return 'rd'
#         case _:
#             return 'th'



# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True