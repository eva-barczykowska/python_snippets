# Let's generalize the function from the previous exercise.
# Implement a function named citethat takes two string arguments:
# the author of the quote and what they said. It then prints the quote, as shown below.

def cite(author, quote):
    return f'{author} said: "{quote}"'


print(cite('Bruce Eckel', 'Python is executable pseudocode.'))
# Bruce Eckel said: "Python is executable pseudocode."

print()
def cite(author, quote):
    print('{} said: "{}"'.format(author, quote))


print(cite('Bruce Eckel', 'Python is executable pseudocode.'))
