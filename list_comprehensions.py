# a way to create a list from scratch
# a concise and readable way to create a lists allowing to define various settings in a single line of code
# with list comprehension, you can apply any expression to each item in the list being created
# you can also incorporate a condition into a list comprehension

# long way
nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)


# short way using list comprehension
# <variable> = [expression for <item> in iterable if <condition>]
# <variable> - will store the newly created list
# <expression> - an expression performed on each item in the iterable, if no action is specified, the item itself is used
# <item> the current item being processed
# < iterable> - the sequence of items we want to iterate over, e.g., a list, tuple, string, set, dictionary
# nums = [x for x in range(1, 51)]

nums = [x for x in range(1, 51)]
print(nums)

# we can apply any expression to each item in the list being created with a list comprehension
# For example, the following code DOUBLES each value in range(10) (explain range in Medium article)
nums = [x * 2 for x in range(10)]
print(nums)


tags = ["travel", "python", "coding", "fun"]
hash_tags = ["#" + x for x in tags]
# "#" + x is an expression that performs string concatenation
print(hash_tags)

tags = ["travel", "python", "coding", "fun"]
hash_tags = {tag: len(tag) for tag in tags}
print(hash_tags)

visited_cities = ["colombo", "bangalore", "bangkok", "mumbai", "prague"]
capitalized_cities = [city.capitalize() for city in visited_cities]
print(capitalized_cities)

# we can incorporate a condition into the list comprehension
users = [ "Brandon", "Emma", "Olivia", "Sophia", "Ava"]
grouped_users = [x for x in users if x[0] == "B"]
print(grouped_users)

users = ["Brandon", "Emma", "Olivia", "Sophia", "Ava"]
grouped_users = [x for x in users if x[0] != "B"]
print(grouped_users)

sports = ["football", "basketball", "cricket", "hockey", "voleyball"]
sports_with_ball = [x for x in sports if "ball" in x]
print(sports_with_ball)

scores = [85, 92, 78, 95, 2]
winners = [x for x in scores if x >= 90]
print(winners)

students_and_their_scores = {"Anna Boleyn": 85, "Bill Gates": 65, "Gabor Mate": 99, "Robert Martin":92}
winners = [x for x in students_and_their_scores.keys() if students_and_their_scores[x] > 65]
print(winners)

student_scores = {"Anna Boleyn": 85, "Bill Gates": 65, "Gabor Mate": 99, "Robert Martin":92}
winners = [(name, score) for name, score in student_scores.items() if score >= 65]
print(winners)
print(dict(winners))

print()

# Using list comprehension to solve the FizzBuzz problem
fizzbuzz = [
    "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
    "Fizz" if num % 3 == 0 else
    "Buzz" if num % 5 == 0 else
    num
    for num in range(1, 21)
]

# The FizzBuzz list is now created and stored in fizzbuzz
print(fizzbuzz)
