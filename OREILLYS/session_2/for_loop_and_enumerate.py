index = 0
for one_character in 'abcd':
    print(f"{index}: {one_character}")
    index += 1

print()
# another way to iterate over a string and get index and character
for index, character in enumerate('abcd'):
    print(f"{index}: {character}")

print()
# index will be ALWYAS first, character will be always SECOND
# enumerate function must take an iterable (like string) as argument
# but it can also take a start parameter, which will be the first index by default

for index, character in enumerate('abcd', 7):
    print(f"{index}: {character}")