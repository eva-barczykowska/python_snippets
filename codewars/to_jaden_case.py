def to_jaden_case(s):
    jadenized = []
    temp_list = s.split()
    print(temp_list)

    for word in temp_list:
        word = word.capitalize()
        jadenized.append(word)
    return ' '.join(jadenized)


import string


def to_jaden_case_optimized(text):
    return string.capwords(text)


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))

quote = "How Can Mirrors Be Real If Our Eyes Aren't Real"
print(to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real")

print(to_jaden_case_optimized(quote))
print(to_jaden_case_optimized(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real")
