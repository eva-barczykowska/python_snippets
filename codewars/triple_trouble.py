# -take each consecutive char from each consecutive word
# -they are all same length
# -use length to get index
# -build a new string with char at each index from each word
# -i.e. char at index 0 from "aaa", index 1 from "bbb", index 2 from "ccc"
def triple_trouble(one, two, three):
    result = ''

    length = len(one)

    for i in range(length):
        result += one[i] + two[i] + three[i]

    return result



print(triple_trouble("aaa", "bbb", "ccc"))  #, "abcabcabc")
print(triple_trouble("aaaaaa", "bbbbbb", "cccccc"))  # , "abcabcabcabcabcabc")
print(triple_trouble("burn", "reds", "roll"))  # , "brrueordlnsl")
print(triple_trouble("Bm", "aa", "tn"))  #, "Batman")
print(triple_trouble("LLh", "euo", "xtr"))  #, "LexLuthor")


def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))


print(triple_trouble("aaa", "bbb", "ccc"))  #, "abcabcabc")
print(triple_trouble("aaaaaa", "bbbbbb", "cccccc"))  # , "abcabcabcabcabcabc")
print(triple_trouble("burn", "reds", "roll"))  # , "brrueordlnsl")
print(triple_trouble("Bm", "aa", "tn"))  #, "Batman")
print(triple_trouble("LLh", "euo", "xtr"))  #, "LexLuthor")