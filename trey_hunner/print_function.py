import datetime

file = open("log.txt", mode="wt")
time = 62.738

print("Time: ", time, file=file) # writes one time only though

#does same thing as above
file.write(f"Time: + {time}\n")

# wt writes text, at appends:
# file = open("log.txt", mode="at")
# time = datetime.datetime.now()
# file.write(f"Time appended is {time}")

with open("log.txt", mode="a") as file:
    file.write(f"Time appended is {datetime.datetime.now()}\n")
    file.write(f"Another line at {datetime.datetime.now()}\n")

print('-----')
numbers = [1, 2, 3, 4, 5]
with open("numbers.txt", mode="wt") as file:
    print("Lucas numbers: ", end="", file=file)
    print(*numbers, sep=", ", file=file)