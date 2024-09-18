# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    passengers = bus_stops[0][0]
    for stop in bus_stops[1:]:  # starting from the second stop, first stop is already accounted for
        passengers += stop[0]
        passengers -= stop[1]

        print(passengers)

    return passengers


print(number([[10, 0], [3, 5], [5, 8]]) == 5)
print(number([[10, 0], [3, 5], [5, 8]]) == 5)
print((number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])))


# another solution

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


print(number([[10, 0], [3, 5], [5, 8]]) == 5)
print(number([[10, 0], [3, 5], [5, 8]]) == 5)
print((number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])))
