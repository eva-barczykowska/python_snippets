def greet(language):
    if language == 'en':
        return 'Hi!'
    elif language == 'fr':
        return 'Salut!'
    elif language == 'pt':
        return 'Olá!'
    elif language == 'de':
        return 'Hallo!'
    elif language == 'sv':
        return 'Hej!'
    elif language == 'af':
        return 'Haai!'


print(greet('en'))  # Hi!
print(greet('fr'))  # Salut!
print(greet('pt'))  # Olá!
print(greet('de'))  # Hallo!
print(greet('sv'))  # Hej!
print(greet('af'))  # Haai!


# another solution

def greet_v2(language):
    greetings = {
        'en': 'Hi!',
        'fr': 'Salut!',
        'pt': 'Olá!',
        'de': 'Hallo!',
        'sv': 'Hej!',
        'af': 'Haai!'
    }
    return greetings.get(language, 'Unknown language')


print(greet('en'))  # Hi!
print(greet('fr'))  # Salut!
print(greet('pt'))  # Olá!
print(greet('de'))  # Hallo!
print(greet('sv'))  # Hej!
print(greet('af'))  # Haai!


# another solution

def greet_v3(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Unknown language'

