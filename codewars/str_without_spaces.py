def no_space(x):
    str_without_spaces = ''

    for one_character in x:
        if one_character == " ":
            continue
        else:
            str_without_spaces += one_character

    return str_without_spaces


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))  # , '8j8mBliB8gimjB8B8jlB')
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))  # , '88Bifk8hB8BB8BBBB888chl8BhBfd')
print(no_space('8aaaaa dddd r     '))  # , '8aaaaaddddr')
print(no_space('jfBm  gk lf8hg  88lbe8 '))  # , 'jfBmgklf8hg88lbe8')
print(no_space('8j aam'))  # , '8jaam')

print()

print()
print("---will this mutate?---")


def no_space(x):
    return x.replace(' ', '')


x = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(x)
print(no_space(x))
print(x)
print()


def no_space(x):
    return "".join(x.split())


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))  # , '8j8mBliB8gimjB8B8jlB')
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))  # , '88Bifk8hB8BB8BBBB888chl8BhBfd')
print(no_space('8aaaaa dddd r     '))  # , '8aaaaaddddr')
print(no_space('jfBm  gk lf8hg  88lbe8 '))  # , 'jfBmgklf8hg88lbe8')
print(no_space('8j aam'))  # , '8jaam')

print()


def no_space(x):
    x = x.replace(" ", "")  # think about mutation
    return x


x = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(x)
print(no_space(x))
print(x)

print()


def no_space(x):
    return ''.join(i for i in x if i != ' ')


x = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(x)
print(no_space(x))
print(x)

print()
