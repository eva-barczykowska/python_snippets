def count_words(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words("oh what a day what a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
print(count_words("don't stop believing"))
# {"don't": 1, 'stop': 1, 'believing': 1}