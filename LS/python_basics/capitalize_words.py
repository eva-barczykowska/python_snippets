# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

str = 'launch school tech & talk'
print(str.title())

# longer solution
def capitalize_words(string):
    words = string.split(' ')
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())

    return ' '.join(capitalized_words)

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk

# shorter solution
def capitalize_words(string):
    return string.title()


string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk