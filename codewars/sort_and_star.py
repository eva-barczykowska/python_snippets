def two_sort(array):
    ordered = sorted(array)
    first_word = ordered[0]
    result = ""
    for idx, letter in enumerate(first_word):
        if idx == len(first_word) - 1:
            result += letter
        else:
            result += letter
            result += "***"


    return result

print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))

def two_sort(lst):
    return '***'.join(min(lst))

print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))