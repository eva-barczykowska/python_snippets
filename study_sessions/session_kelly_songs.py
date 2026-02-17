# Implement a function that takes two numbers m and n and returns an array of the first m multiples of the real number n. Assume that m is a positive integer.
#
# (3, 5.0) --> [5.0, 10.0, 15.0]
# 5*1
# 5*2
# 5*3

def multiples(m: int, n: int | float) -> list[int] | list[float]:
    my_list = []
    for range_number in range(1, m + 1):
        my_list.append(range_number * n)
    return my_list

print(func(3, 5.0))

# class Warehouse:


#     def __init__(self, name):
#         self.name = name
#         self.items = []

#     def add_item(self, item_name):
#         self.items.append(item_name)

#     def show_items(self):
#         print(f"{self.name} Warehouse contains: {self.items}")

# wh1 = Warehouse("Seattle")
# wh2 = Warehouse("New York")

# wh1.add_item("Laptop")
# wh2.add_item("Mouse")

# wh1.show_items()
# wh2.show_items()

# # Expected Output:
# # Seattle Warehouse contains: ['Laptop']
# # New York Warehouse contains: ['Mouse']

# # Actual Output:
# # Seattle Warehouse contains: ['Laptop', 'Mouse']
# # New York Warehouse contains: ['Laptop', 'Mouse']

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         return f"{self.make} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, make, model, battery_size):
#         super().__init__(make, model)
#         self.battery_size = battery_size

#     def display_info(self):
#         # This line will cause an error
#         return f"{super().display_info()} with a {self.battery_size}kWh battery"

# my_tesla = ElectricCar("tesla", "500", 100)
# # The following line raises an AttributeError
# print(my_tesla.display_info())

# The Point class is meant to represent a 2D coordinate. The __eq__ method is implemented to check for equality between two Point objects. However, comparing a Point object to a non-Point object crashes the program with an AttributeError. Modify __eq__ to correctly handle comparisons with other types.

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         if not isinstance(other, Point):
#              return NotImplemented
#         return self.x == other.x and self.y == other.y

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# p3 = (1, 2)

# print(p1 == p2) # Expected: True
# # The following line raises an AttributeError
# print(p1 == p3) # Expected: False

#A RoboticDog class inherits from Robot and Dog. Both parent classes have a speak method. The intention is for RoboticDog to use the Robot's speak method, but it's using the Dog's method instead. Fix the class definition without changing the method bodies.

# class Robot:
#     def speak(self):
#         return "I am a robot."

# class Dog:
#     def speak(self):
#         return "Woof!"

# class RoboticDog(Robot, Dog):
#     pass


# barki = RoboticDog()
# print(barki.speak()) # Expected: "I am a robot."
#                       # Actual: "Woof!"

# print(list(RoboticDog.mro()))

# The Temperature class uses a property to manage temperature in Celsius. The setter for the celsius property is supposed to prevent temperatures below absolute zero (-273.15 C), but the check is flawed and raises a ValueError for all negative temperatures.

# class Temperature:


#     def __init__(self, celsius):
#         self.celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#              raise ValueError("Temperature below absolute zero is not possible.")
#         self._celsius = value

# t = Temperature(10)
# print(t.celsius)

# # The following line should work, but it raises a ValueError
# t.celsius = -10
# print(t.celsius)

# # The following line should raise a ValueError
# t.celsius = -300
# print(t.celsius)


#The Playlist class holds a list of Song objects. The add_song method is supposed to add a song to the playlist's list. However, it's modifying the list directly and returning it, which is an unconventional pattern. The major issue is that if add_song fails (which it does if the song is already in the playlist), it returns None, causing a TypeError in the calling code. Fix the add_song method to be more robust and conventional.

class Song:
    def __init__(self, title):
        self.title = title


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or []


    def add_song(self, song):
        if song in self.songs:
            return self.songs
        else:
            self.songs.append(song)
            return self.songs


# Calling code
playlist = Playlist("My Jams")
print(playlist.name)
song1 = Song("Bohemian Rhapsody")
song2 = Song("Stairway to Heaven")

playlist.songs = playlist.add_song(song1)
playlist.songs = playlist.add_song(song2)
print(playlist.name)


# This call returns None because the song is a duplicate
playlist.songs = playlist.add_song(song1)

# The next line raises a TypeError because playlist.songs is now None
print(len(playlist.songs))