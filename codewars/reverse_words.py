# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    words = s.split()

    reversed_words = " ".join(words[::-1])
    print(reversed_words)  # debug

    return reversed_words


print(reverse_words("hello world!") == "world! hello")
print(reverse_words('This is so easy') == 'easy so is This')
print(reverse_words('no one cares') == 'cares one no')
print(reverse_words('') == '')
print(reverse_words('CodeWars') == 'CodeWars')

print('--------------------------')
def reverse_words(s):
    words = s.split()

    words.reverse() # reverse returns None and is mutating!!!

    return " ".join(words)


print(reverse_words("hello world!") == "world! hello")
print(reverse_words('This is so easy') == 'easy so is This')
print(reverse_words('no one cares') == 'cares one no')
print(reverse_words('')) #== '')
print(reverse_words('CodeWars') == 'CodeWars')
