colors = ["purple", "pink", "blue"]
animals = ["duck", "flamingo", "unicorn"]
for i in range(len(colors)):
    print(colors[i], animals[i])


print()
# better:
for color, animal in zip(colors, animals):
    print(color, animal)

colors = ["purple", "pink", "blue"]
for i in range(len(colors), 0, -1):
    print(colors[i-1])
print()

# better:
for color in reversed(colors):
    print(color)