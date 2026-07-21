
zeme = ["chorvatsko", "slovensko", "polsko", "madarsko"]
slova = ["jagoda", "nabytek", "chorvatsko"]

# for cycle example
for slovo in slova:
    for jedna_zeme in zeme:
        if slovo in zeme:
            print(slovo.title())

# print("---")
# # function example
# def find_in_zeme(zeme, slova):
#     spolecne = set(slova) & set(zeme) # find common elements between two sets
#     print(spolecne)
#     print(list(spolecne)[0].title())
#
#
# find_in_zeme(zeme, slova)