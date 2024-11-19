def check_alive(health):
    if health > 0:
        return True
    else:
        return False


print(check_alive(10))  # True
print(check_alive(0))  # False


def check_alive(health):
    return health > 0


print(check_alive(10))  # True
print(check_alive(0))  # False
