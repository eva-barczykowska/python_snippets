# I Want to Remove Duplicates from a Python List • How Do I Do It?

queue = ["James", "Kate", "Andy", "James", "Isabelle", "Kate"]

queue_unique = []
for index, name in enumerate(queue):
    if name not in queue[index + 1:]: # very interesting
        queue_unique.append(name)


print(queue_unique)
#['Andy', 'James', 'Isabelle', 'Kate']

# 0, end
# 1, end
# 2, end
# I found it interesting that the element is added only if it is not found in the list after the current index.
# Note that the customers/names are NOT in original order.

queue = ["James", "Kate", "Andy", "James", "Isabelle", "Kate"]
unique_set = set(queue)
print(unique_set)
unique_list = list(unique_set)
print(unique_list)


queue = ['James', 'Kate', 'Andy', 'James', 'Isabelle', 'Kate']
queue.reverse() # ['Kate', 'Isabelle', 'James', 'Andy', 'Kate', 'James']


queue_unique = queue.copy() # ['Kate', 'Isabelle', 'James', 'Andy', 'Kate', 'James']

for index, name in enumerate(queue): # ['Kate', 'Isabelle', 'James', 'Andy', 'Kate', 'James']
    if name in queue[index + 1:]:
        queue_unique.remove(name) # remove removes ONLY THE FIRST occurrence of the element


queue_unique.reverse()
queue_unique # ['James', 'Kate', 'Andy', 'Isabelle']
# this was similar idea but not adding, removing

# However, there's an issue. If this is a queue of customers, then the order in which they joined the queue is somewhat important, I would say!


# this is HOW we will preserve order while removing duplicates

queue = ['James', 'Kate', 'Andy', 'James', 'Isabelle', 'Kate']
print(dict.fromkeys(queue)) # {'James': None, 'Kate': None, 'Andy': None, 'Isabelle': None}
queue_unique = list(dict.fromkeys(queue).keys())
print(queue_unique)

# limitation
# Both the set and dictionary routes have an important limitation.
# Items in a set must be hashable objects. And keys in a dictionary must also be hashable.
# Therefore, you can't use these techniques if you have a list that includes non-hashable objects,
# such as a list that contains other lists.