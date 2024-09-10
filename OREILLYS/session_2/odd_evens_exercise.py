# Exercise: Odds and evens
# Define two empty lists, odds and evens.
# We're going to ask the user to enter 5 numbers.
# For each input, check that it's numeric and can be turned into an int. (If not, scold the user.)
# Check if the number is odd or even.
# If it's odd, append to odds
# If it's even append to evens
# When you're done, print both lists.
# Example:
#
# Enter number 0: 15
# Enter number 1: 23
# Enter number 2: 88
# Enter number 3: exit
#     exit is not numeric; try again
# Enter number 4: 7
# odds: [15, 23, 7]
# evens: [88]


odds = []
evens = []
counter = 1
numbers = []


while counter <= 5:
    number = input(f"Please enter 5 numbers: Enter number {counter}: ")
    if not number.isdigit():
        print(f"Input not numeric; try again")
        continue
    else:
        if int(number) % 2 == 0:
            evens.append(int(number))
        else:
            odds.append(int(number))
    counter += 1


print(f"odds: {odds}")
print(f"evens: {evens}")