def title_case(title, minor_words=''):
    minor = set(minor_words.lower().split(' '))
    print(minor)
    lowercase_title = title.lower()

    final_title = []
    for word in lowercase_title.split(" "):
        if word in minor:
            final_title.append(word)
        else:
            capitalized = word.title()
            final_title.append(capitalized)

    joined_title = ' '.join(final_title)

    return joined_title[0].capitalize() + joined_title[1::]

# fails when title is ''
print(title_case('a clash of KINGS', 'a an the of'))

# fixed

def title_case(title, minor_words=''):
    if title == '':
        return ''
    else:
        minor = set(minor_words.lower().split(' '))
        print(minor)
        lowercase_title = title.lower()

        final_title = []
        for word in lowercase_title.split(" "):
            if word in minor:
                final_title.append(word)
            else:
                capitalized = word.title()
                final_title.append(capitalized)

        joined_title = ' '.join(final_title)

        return joined_title[0].capitalize() + joined_title[1::]

def title_case(title, minor_words=''):
    minor = set(minor_words.lower().split())
    words = title.lower().split()
    final_title = [w if w in minor else w.title() for w in words]
    joined = ' '.join(final_title)
    return joined[0].upper() + joined[1:]


print(title_case('a clash of KINGS', 'a an the of'))