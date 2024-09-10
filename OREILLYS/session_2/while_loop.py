total = 0

while total < 100:
    number = input("Enter a number: ")
    if not number.isdigit():
        number = input("Input not numeric; try again: ")
    else:
        total += int(number)


print("You've reached the total of 100!")
