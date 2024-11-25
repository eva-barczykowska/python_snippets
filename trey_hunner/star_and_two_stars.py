# There's * for unpacking iterables as positional arguments function calls:
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
numbers = [2, 1, 3, 4, 7]
print(*numbers, *fruits)  # * basically means all
# 2 1 3 4 7 lemon pear watermelon tomato

# And ** for unpacking mappings as named arguments into function calls:
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
     **date_info,
     **track_info,
 )
print(filename)  #'2020-01-01-Beethoven-Symphony No 5.txt'

# And ** in function definitions for capturing named arguments:
def tag(tag_name, **attributes):
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"

# You can also put arguments after * captures in function definitions for designating keyword-only arguments:
def get_multiple(*keys, dictionary, default=None):
    return [
        dictionary.get(key, default)
        for key in keys
    ]


# And there's even a lone * syntax, which looks a little odd:
def with_previous(iterable, *, fillvalue=None):
    """Yield each iterable item along with the item before it."""
    previous = fillvalue
    for item in iterable:
        yield previous, item
        previous = item


# The * operator can also be used for packing iterables in tuple unpacking:
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
((first_letter, *remaining), *other_fruits) = fruits
print(remaining)  # ['e', 'm', 'o', 'n']
print(other_fruits)  # ['pear', 'watermelon', 'tomato']


# The * operator also works in list/set/tuple literals:
def palindromify(sequence):
    return [*sequence, *reversed(sequence)]


# And the ** operator can also be used in dictionary literals:
event_info = {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}
new_info = {**event_info, 'day': "14"}
print(new_info)  # {'year': '2020', 'month': '01', 'day': '14', 'group': 'Python Meetup'}