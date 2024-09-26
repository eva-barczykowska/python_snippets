def status_report():
    return 10, {'status': 'OK', 'reported_at': 'Thu-Sep-19'}  # this is actuall a tuple


print(status_report())

t = status_report()

status_grade = t[0]  # we can unpack the tuple into variables
status_details = t[1]

print(status_details["reported_at"])

# even better:

status_grade, status_details = status_report()

print(status_grade)
print(status_details)


# returning complex objects
# you can return any object, not just tuples

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


# another way with setting up the dict first
def count_chars_v2(text, chars):
    count = {}
    for char in chars:
        count[char] = 0

    for char in text:
        if char in chars:
            count[char] += 1

    return count


count_hash = count_chars_v2("Two to five!", "aeoui")
print(count_hash)


# another example
def count_chars_v3(chars, to_count='aeoui'):
    tally = {}
    for one_character in chars:
        if one_character in to_count:
            tally[one_character] = tally.get(one_character, 0) + 1
    return tally


result = count_chars_v3("Annual", "aeoui")
print(result)

print('version 4')


# nested if
def count_chars_v4(text, to_count='aeoui'):
    count = {}

    for char in text:
        if char in to_count:
            if char in count:
                count[char] += 1
            else:
                count[char] = 0

    return count


result = count_chars_v4("panda", "panda")
print(result)

print('version 5')


# another example
def count_chars_v5(text, to_count='aeoui'):
    result = {}
    for a_character in text:
        if a_character in to_count:
            result[a_character] = text.count(a_character)
        else:
            result[a_character] = 0
    return result


result = count_chars_v5("panda", "panda")
print(result)

print('version 6')


# refactored:
def count_chars_v6(text, to_count='aeoui'):
    result = {}

    for a_character in to_count:
        result[a_character] = text.count(a_character)

    return result


r = count_chars_v6("helium", "aeoiui")
print(r)
