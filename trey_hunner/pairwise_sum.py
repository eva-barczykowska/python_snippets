def pairwise_sum(lst1, lst2):
    """lst 1 and lst2 are lists of ingegers and are of the same length."""
    sum_pairs = []
    for i in range(len(lst1)):
        sum_pairs.append(lst1[i] + lst2[i])

    return sum_pairs

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(pairwise_sum(lst1, lst2))  # Output: [5, 7, 9]