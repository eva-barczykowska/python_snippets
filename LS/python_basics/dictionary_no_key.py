info = {'name': 'Srdjan', 'age': 38}

target = info.get('city', "Unknown") # second argument is the default value in case the key is not found

print(target)