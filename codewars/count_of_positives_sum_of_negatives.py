# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
# -how many positive numbers do we have?
# -how many negative numbers do we have?
# -zero is neither positive nor negative

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    else:
        positive = 0
        negative = 0

        for num in arr:
            if num > 0:
                positive += 1
            elif num < 0:
                negative += num

    return [positive, negative]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  #, [10, -65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))  #, [8, -50])
print(count_positives_sum_negatives([1]))  #, [1, 0])
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))  #, [0, 0])
print(count_positives_sum_negatives([]))  #, [])


# comprehension list

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        positive = sum(1 for num in arr if num > 0)
        negative = sum(num for num in arr if num < 0)

    return [positive, negative]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  #, [10, -65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))  #, [8, -50])
print(count_positives_sum_negatives([1]))  #, [1, 0])
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))  #, [0, 0])
print(count_positives_sum_negatives([]))  #, [])


# my fav

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  #, [10, -65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))  #, [8, -50])
print(count_positives_sum_negatives([1]))  #, [1, 0])
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))  #, [0, 0])
print(count_positives_sum_negatives([]))  #, [])
