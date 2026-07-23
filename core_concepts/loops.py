s = 'abcd'
for char in s:
    print(char)

print('--------------')
for char in s:
    print(char.upper())

print('--------------')


for char in s:
    print(ord(char))

print('--------------')

for char in s:
    print(chr(ord(char) + 1)) # shift like you want to decifer or encrypt

print('--------------')