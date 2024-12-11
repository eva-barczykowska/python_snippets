# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'

str = 'Captain Ruby'
transformed = str[0:7] + ' Python'
print(transformed)

print()

text = 'Captain Ruby'
s = slice(0, 7)
print(text[s] + 'Python')

print()

first_8 = 'Captain Ruby'[:8] # cutting also the space!
new_str = first_8 + 'Python'
print(new_str)      # Captain Python

print()

all_words = 'Captain Ruby'.split(' ')
first_word = all_words[0]
new_str = first_word + ' Python'
print(new_str)      # Captain Python

new_str = 'Captain Ruby'.replace('Ruby', 'Python')
print(new_str)      # Captain Python
