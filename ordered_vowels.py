"""
Write a function that takes a list of words and returns a new list containing only the words where the vowels (a, e, i, o, u)
appear in alphabetical order. The vowels within a word do not need to be consecutive, but their sequence must be
sorted alphabetically. Case is not important.
"""

def find_ordered_vowel_words(list_of_words):
    result = []
    temp_result = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in list_of_words:
        # chars = [char for char in word]
        chars = list(word) # collection constructor call is considered better
        # print(chars)
        for char in chars:
            if char in vowels:
                temp_result.append(char)

            if temp_result == vowels:
                result.append(word)
                temp_result = []

    return result


words1 = ["facetious", "abstentious", "sequoia", "education", "computer"]
# 'facetious' -> a, e, i, o, u -> sorted
# 'abstentious' -> a, e, i, o, u -> sorted
# 'sequoia' -> e, u, o, i, a -> not sorted
# 'education' -> e, u, a, i, o -> not sorted
# 'computer' -> o, u, e -> not sorted
# Expected output: ["facetious", "abstentious"]
print(find_ordered_vowel_words(words1))

words2 = ["dialogue", "aeonian", "beautiful"]
# 'dialogue' -> i, a, o, u, e -> not sorted
# 'aeonian' -> a, e, o, i, a -> not sorted
# 'beautiful' -> e, a, u, i, u -> not sorted
# Expected output: []
print(find_ordered_vowel_words(words2))

# Expected output: []
print(find_ordered_vowel_words([]))

