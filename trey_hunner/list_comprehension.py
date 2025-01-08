screencasts = [
    "Data structures contain pointers",
    "What is self?",
    "What is a class?",
    "Slicing",
    "How to make a function",
    "Methods are just functions attached to classes",
    "Method is just a function that belongs to a class, method is a function that lives on a class",
]
print("original list:")
print(screencasts)
# transform the list into a list of titles
titles = []
for screencast in screencasts:
    titles.append(screencast.title())

print("printing the filled titles list after running the loop:")
print(titles)
print("original list:")
print(screencasts)

titles_optimized = [screencast.title() for screencast in screencasts] # appending happens automatically
print("after list comprehension:")
print(titles_optimized)
print("original list:")
print(screencasts)

titles = [                         # really like this way of writing list comprehension --------------------------------
    screencast.title()
    for screencast in screencasts
]

# more clear than ------ titles = [name.title() for name in screencasts]

# filtering the list
long_names = []
for name in titles:
    if len(name) > 30:
        long_names.append(name[:30] + "...")

print("long names:")
print(long_names)

# list comprehension with filtering
long_names_optimized = [
    name[:30] + "..."
    for name in titles
    if len(name) > 30
]
print("long names (optimized):")
print(long_names_optimized)

# written in multiple lines is more readable than this:
long_names = [name[:27] + "..." for name in titles if len(name) > 30]

print()

famous_titles = [
    "1984",
    "The Hitchhiker's Guide to the Galaxy",
    "Emma",
    "Dune",
    "The Curious Incident of the Dog in the Night-Time",
    "Frankenstein",
    "The Guernsey Literary and Potato Peel Pie Society",
    "The Adventures of Sherlock Holmes",
    "Dracula",
    "The Girl with the Dragon Tattoo"
]

long_titles = [
    title[:20] + "..."
    for title in famous_titles
    if len(title) > 30
]

# rather than one line
long_titles = [title[:20] + "..." for title in famous_titles if len(title) > 30]

print(long_titles)
