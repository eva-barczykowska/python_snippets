# The first input array is the key to the correct answers to an exam,
# like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.
#
# The two arrays are not empty and are the same length.
# Return the score for this array of answers, giving +4 for each correct answer,
# -1 for each incorrect answer, and +0 for each blank answer,
#
# If the score < 0, return 0.

# Correct
# answer | Student
# 's answer   |   Result
# --------------------- | ----------------------- | -----------
# ["a", "a", "b", "b"]["a", "c", "b", "d"]  →     6
# ["a", "a", "c", "b"]["a", "a", "b", ""]  →     7
# ["a", "a", "b", "c"]["a", "a", "b", "c"]  →     16
# ["b", "c", "b", "a"]["", "a", "a", "c"]  →     0

# PEDAC
# -iterate over the arrays simultaneously
# -the 2 lsts are of equal length
# -compare corresponding elements
# -if they match, add 4 to the score-if they don't match, subtract 1 from the score
# -if any element is an empty string, add 0 to the score
# -if the score is negative, return 0
# -if the score is positive, return the score
# -else return 0

# Examples:
# ["a", "a", "b", "b"]["a", "c", "b", "d"]  →     6
# ["a", "a", "c", "b"]["a", "a", "b", ""]  →     7
# ["a", "a", "b", "c"]["a", "a", "b", "c"]  →     16
# ["b", "c", "b", "a"]["", "a", "a", "c"]  →     0

# Algorithm
# -prepare indices - numbers from 0 to length of arr1 - 1
# - initialize score to 0
# - iterate over indices in both array and compare elements at those indices:
# --if they match, add 4 to the score
# --if they don't match, subtract 1 from the score
# --if any element is an empty string, add 0 to the score
#
# finally if the score is equal or less than 0 na, return 0
# if the score is positive, return the score

def check_exam(arr1, arr2):
    score = 0

    indices = list(range(len(arr1)))
    for i in indices:
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] != arr2[i] and arr2[i] != "":  # if arr2[i] is not empty, it means it's incorrect, so subtract 1 from the score'
            score -= 1
        elif arr2[i] == "":
            score += 0

    return score if score >= 0 else 0


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))  # , 6)
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))  # , 7)
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))  # , 16)
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))  # , 0)


def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))  # , 6)
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))  # , 7)
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))  # , 16)
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))  # , 0)

print()
def check_exam(arr1, arr2):
    return list(zip(arr1, arr2)) # but now it's a list of tuples
    # return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))  # , 6)