quantities = {"pink": 3, "green": 4}
if "blue" not in quantities:
    print("Blue does not exist as a key in the dictionary.")

color = "blue"
if color not in quantities:
    print(f"Uh oh! There's no value for {color}")

color = "gold"
count = quantities.get(color, 0)  # Returns 0 if color is not in dictionary
print(f"The {color} color has {count} quantities.")

color = "silver"
count = quantities.get(color)  # Returns None if color is not in dictionary
print(f"The {color} color has {count} quantities.")
