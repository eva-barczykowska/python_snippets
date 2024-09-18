# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    if not lines:
        return []
    else:

        formatted = []
        counter = 1
        for line in lines:
            formatted.append(f"{str(counter)}: {line}")
            counter += 1

    return formatted

def number(lines):
    return [f"{i}: {j}" for i,j in enumerate(lines,1)] 


print(number([])) #, [])
print(number(["a", "b", "c"]))#, ["1: a", "2: b", "3: c"])