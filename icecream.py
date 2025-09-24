try:
    from icecream import ic
except Exception:  # Fallback if 'icecream' is not installed
    def ic(*args, **kwargs):
        # Simple fallback that mimics basic output of icecream.ic
        print(*args)

def add(a, b):
    result = a + b
    print(f"result is {result}")
    ic(result)
    return result

if __name__ == "__main__":
    add(3, 4)

    # no need for icecream!

    x = 10
    y = 20
    z = x + y

    print(f"{x=}, {y=}, {z=}")
