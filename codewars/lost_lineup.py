# https://www.codewars.com/kata/6914c975e159c8f7e120cc84/train/python

# Problem:
# -restore the original order of the q
# -input, element i is the number of ppl i remembers between them and Carol []
# -output [] original q BUT Carol is not included here (since she was the first)

# EX:
#   input:  [1, 2, 0], index is the person, int at the index is the NUMBER OF PPL between Carol and that person(index!)
#   output: [3, 1, 2], we are putting index of 0 in one place coz there was 0 ppl between that person(index 3) and Carol

#    input: [1, 0, 1]
#    output: []

# A:
#     -iterate over the input list
#     -check the lowest number
#     -append its index to the `fixed_q array`
#     -delete that number from the array BAD BAD IDEA!!! (to iterate and delete at the same time, indexes will be skipped)
#     -but I guess I could just take it
#     -append its index to the `fixed_q array`

# A2:
# -save nums and indices to a dict
# -index is the key and int is the value
# -if 2 values are same, return []
# -if values are less than 1, return []
# -if any of the values is greater than 100, return []
# [1, 2, 0] -> [3, 1, 2]
# {0:1, 1:2, 2:0}
# look for the smallest value, 0
# take its index, 3
# append it to the `fixed_queue`, repeat
# increase the smallest value by 1
# find it in the input array
# again, append it to the `fixed_queue`, do until no more nums left


# A3
# ALSO possible to sort by values {0:1, 1:2, 2:0} -> {2:0, 0:1, 1:2}, take each key, add 1 and insert to the `fixed_queue`

# iterate over the hash and insert in the `fixed_queue` the INDEX of the least

# Constraints:
#    -if 2 nums are same, return []
# -1 ≤ n ≤ 100 number will be greater than or equal to 1 AND less than/equal to 100


# def find_lineup(distances):
#     if any(d < 0 or d > 100 for d in distances):
#         return []
#     else:
#         fixed_queue = []
#         distances_dict = dict(distances)
#         sorted_distances = sort(distances, lambda pair: pair[1])
#         for key, value in sorted_distances:
#             fixed_queue.append(key)
#
#     return fixed_queue
#
#
# print(find_lineup([[1, 2, 0]]))


distances = [1, 2, 0]
if any(distances):
    print('done')