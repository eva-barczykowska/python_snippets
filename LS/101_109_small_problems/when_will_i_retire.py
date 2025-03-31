# When Will I Retire?
# Build a program that displays when the user will retire and how many years she has to work till retirement.
from datetime import date
age = int(input("What is your age?"))
wish_retire = int(input("What age would you like to retire"))

how_many_years_left = wish_retire - age

year_now = date.today().year
print(f"It is {year_now}, you have {how_many_years_left} years")
#What is your age? 30today()
#At what age would you like t retire? 70

#It's 2024. You will retire in 2064.
#You have only 40 years of work to go!