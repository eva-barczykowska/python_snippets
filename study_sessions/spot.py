# https://github.com/The-SPOT-Hub/SPOT-Wiki/blob/main/Lesson%20Materials%20%26%20Code/PY101/Python101.md
# 1. What does this print and why?

# mashup = "thIs is How we type careLEssly"
# cleaned = mashup.capitalize() #title
# # cleaned = mashup.title()
# print(cleaned)

###

# What is the output of this code, and why? What is the concept covered here?

# str1 = "Hello, world!"
# sub1 = str1[8:12] # "orld"
# print(sub1)
# sub2 = str1[::-1] # "Hello, world!" backwards
# print(sub2)
# sub3 = str1[::2] # "Hlo ol!" "Hlo ol!
# print(sub3)

# s1 = "Hello"
# print(s1.isalpha()) #True # True

# s2 = "Hello World"
# print(s2.isalpha()) #True space? # True FALSE!!!

# s3 = "Hello!"
# print(s3.isalpha()) #False # False FALSE!!!

# s4 = "Hello123"
# print(s4.isalpha()) #True # False .isalnum FALSE!!!

# s5 = ""
# print(s5.isalpha()) #False # False FALSE!!!

# s6 = "こんにちは"
# print(s6.isalpha()) #True # False TRUE
# s7 = "HelloWorld"
# print(s7.isalpha()) #True # True

# words = ["apple", "banana", "cherry"]
# print(all(word.isalpha() for word in words)) # [True, True, True] # True TRUE!

# returns true only if all chars are alphabetic
# alphabetic = letters in pretty much any language (unicode), not just a–z
# # digits, spaces, punctuation, emojis, etc → instant false

# num = 12

# if num / 3 < 3 and num > 10:
#     print("Hello")
# elif num >= 8 and num < 6 or num > 4 and num < 16:
#     print("Hello 2")
# elif num % 4 == 0 or num < 7 and num < 10:
#     print("Hello 3")
# else:
#     print("Buy")

# s = "   Hello, World!   "
# print(s.strip())
# print(s.strip(" !")) #"   Hello, World   "

# s1 = "***Hello*LS!***"
# print(s1.strip("!*")) #

# What do these print and why? What concept does this demonstrate?

# print(range(0,10)) # (0...9) #range(0, 10)
# print(len(range(5, 15))) # 10
# # print(my_range[1]) # Variable not created yet error
# print(str(range(3, 7))) # '3, 4, 5, 6' # 'range(3, 7)'
# print(list(range(12, 8, -1))) # [12, 11, 10, 9]
# print(list(range(5, 5, 1))) # []
# print(5 in range(5)) # True
# print(5 not in range(5, 10)) # False

# range(5)

# s = "www.example.com"
# print(s.lstrip('wcmo.')) # example.com

# What does this print and why?

# ages = {
#     "dimo": 31,
#     "olena": 32,
#     "tetiana": 28
# }

# def get_val_of_dimo(info):
#     try:
#         info['dimo']
#         return info['dimo'] # 31
#     except KeyError:
#         return "Typo"

# print(get_val_of_dimo(ages)) # 31

# temperature = 25
# time_of_day = "morning"

# if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
#     print("It's a pleasant day!")
# else:
#     print("It's either too hot or not the right time of day.")

# print(str(range(3, 7)))

def punctuation_type(str):
    if str == str.upper():
        print('This is all caps')
    elif str == str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1) # 'This is all caps'
punctuation_type(str2) # 'This is all lowercase'
punctuation_type(str3) # 'Neither'

# https://learning.oreilly.com