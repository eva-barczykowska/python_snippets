# def to_freud(sentence):
#     explanation_to_everything = ""
#     if sentence == None:
#         return explanation_to_everything
#     elif sentence == "":
#         return explanation_to_everything
#     else:
#         sentence = sentence.split()
#         explanantion_to_everything = []
#         for word in sentence:
#             explanantion_to_everything.append("sex")
#     return " ".join(explanantion_to_everything)
#
# print(to_freud("I love programming"))
# print(to_freud(""))
# print(to_freud(None))


def to_freud(sentence):
    return ' '.join('sex' for _ in sentence.split())

print(to_freud("I love programming"))
print(to_freud(""))