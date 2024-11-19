def problem(a):
    return "Error" if isinstance(a, str) else a * 50 + 6


print(problem(10))  # Output: 506
print(problem("10"))


def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


print(problem(10))  # Output: 506
print(problem("10"))


def problem(a):
    return "Error" if a == str(a) else a * 50 + 6


print(problem(10))  # Output: 506
print(problem("10"))
