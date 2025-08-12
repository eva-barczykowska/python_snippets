# it's a list of dictionaries

""" How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?
"""

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

# -i have a list
# - i have a dict
# - find the key (by the value)
# -sort

# iterate?

# for one_dict in books:
#     print(one_dict['published'])

# # print(sorted(list(books)))
# print(sort(books)))

# books.sort()
# print(books)
# print(books.items())

def get_year(my_dict):
    years = []
    for one_dict in my_dict:
        years.append((int(one_dict['published'])))
    return sorted(years) # return sorted years

# print(get_year(books))


# -we iterate over the returned list   [800, 1869, 1967]
# -each time we call sorted(books, key=get_year), passing the year that is our at our current iteration
# -add that dict to a new array

sorted_books = []
for a_year in get_year(books): #[800, 1869, 1967]
    for one_dict in books:
        if int(one_dict['published']) == a_year:
            sorted_books.append(one_dict)
print(sorted_books)

# AI solution:
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
sorted_books = sorted(books, key=lambda book: int(book['published']))
print(sorted_books)
