def count_chars(text, chars):
    """Expects: a string and a string of characters to be counted.
    Modifies: nothing.
    Returns a dictionary with the count of each character in the string."""
    result = {}
    for char in chars:
        if char in chars:
            result[char] = text.count(char)
    return result


count_hash = count_chars("Hello, World!", "aeoui")
print(count_hash)

print()
print("with a default argument")


def count_chars(text, chars='aeoui'):
    """Expects: a string and (otional) string of characters.
    If no characters are provided, it defaults to 'aeioui' (vowels).
    Modifies: nothing.
    Returns a dictionary with the count of each character in the string."""
    result = {}
    for char in chars:
        if char in chars:
            result[char] = text.count(char)
    return result


count_hash = count_chars("Hello, World!")
print(count_hash)
