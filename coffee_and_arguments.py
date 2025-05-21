# taken from https://www.thepythoncodingstack.com/p/python-function-parameters-arguments-args-kwargs-optional-positional-keyword?utm_source=publication-search
def brew_coffee(coffee_type, strength, milk):
    print(f"Brewing {coffee_type}, strength {strength} and milk {milk}.")

# brew_coffee("Cappuccino", 4, 2)
# # the position is important, if I do
# brew_coffee("Cappuccino", 2, 4)
# # the customer will complain that he got the weakest coffee ever!!!

# if we want to make the function more flexible, we can use keyword arguments while invoking the function
brew_coffee(strength=4, milk=2, coffee_type="Cappuccino")

# type hints can also be used to make the function more understandable
# def brew_coffee(coffee_type: str, strength: int, milk: int):
#     print(f"Brewing {type}, strength {strength} and milk {milk}.")

# difference between DEFAULT and KEYWORD arguments?
# The way you are calling the function here:
#
# ```python
# brew_coffee(strength=4, milk=2, coffee_type="Cappuccino")
# ```
#
# — uses **keyword arguments**. can also be called **NAMED arguments**.
#
# ### Explanation
#
# - **Keyword arguments** are HOW YOU CALL A FUNCTION: you specify the parameter names explicitly in the function call (e.g., `strength=4`). This allows you to pass arguments in any order and makes your code more readable[1][2][4][5][6].
# - **Default arguments** are HOW YOU DEFINE A FUNCTION: you assign default values to parameters in the function definition, so if you don’t provide a value when calling the function, the default is used[1][2][5][6].
#
# **Example:**
#
# ```python
# def brew_coffee(strength=3, milk=1, coffee_type="Espresso"):  # default arguments
#     pass
#
# brew_coffee(strength=4, milk=2, coffee_type="Cappuccino")     # keyword arguments
# ```
# so they look the same but WHERE THEY ARE, makes a difference.

# - In the function definition, `strength=3`, `milk=1`, and `coffee_type="Espresso"` are **default arguments**.
# - In the function call, `strength=4, milk=2, coffee_type="Cappuccino"` are **keyword arguments**[1][2][4][5][6].
#
# **Summary:**
# - **Default arguments** = values set in the function definition.
# - **Keyword arguments** = how you pass values by name when calling the function.
#
# You can use keyword arguments whether or not the function parameters have default values[1][2][4].

# and what are POSITIONAL arguments?
# **Positional arguments** are arguments that are passed to a function in the order in which the parameters are defined in the function declaration. Their values are assigned to the corresponding parameters based solely on their position, not their names[1][2][3][4][5][7].
#
# ### Example
#
# ```python
# def add(x, y):
#     return x + y
#
# result = add(10, 20)  # 10 is assigned to x, 20 is assigned to y
# ```
# Here, `10` is the first positional argument (assigned to `x`), and `20` is the second (assigned to `y`). The order matters: `add(20, 10)` would assign `20` to `x` and `10` to `y`, giving a different result[1][2][4].

### Key Points

# - **Order matters:** The first value goes to the first parameter, the second to the second, and so on[1][2][3][4].
# - **All required positional arguments must be provided:** If you omit one, Python will raise an error[1].
# - **You cannot skip or reorder them without using keyword arguments.**
#
# ### Difference from Keyword Arguments
#
# - **Positional:** `add(10, 20)`
# - **Keyword:** `add(y=20, x=10)` (order doesn't matter with keywords)
#
# ### Summary Table
#
# | Type                | How passed                  | Order matters? |
# |---------------------|----------------------------|---------------|
# | Positional argument | `func(1, 2)`               | Yes           |
# | Keyword argument    | `func(a=1, b=2)`           | No            |


def brew_coffee(coffee_type, strength, milk):
    print(f"coffee is {coffee_type}\n")
    print(f"strength is {strength}\n")
    print(f"milk is {milk}")

brew_coffee("Macchiato", 1, 4)

# keyword arguments can be used to pass arguments in any order, we write argument=value
# that way python knows which argument we are referring to

# but what about if we need more arguments? Like different syrups and add-ons?
def brew_coffee_with_options(coffee_type, strength, milk, *args): # *args is a TUPLE
    print(f"{args=}")
    print(type(args))
    print(
        f"coffee is {coffee_type}\n"
        f"strength is {strength}\n"
        f"milk is {milk}\n"
        f"Add-ons: {', '.join(args)}"
    )

# now this function can accept any number of add-ons - any number of positional arguments following the first 3
brew_coffee_with_options("Cappuccino", 1, 4, "Vanilla", "Caramel")

# we don't have to use *args, we can use *add-ons
def brew_coffee_with_options(coffee_type, strength, milk, *add_ons): # *args is a TUPLE
    print(f"{add_ons=}")
    print(type(add_ons))
    print(
        f"coffee is {coffee_type}\n"
        f"strength is {strength}\n"
        f"milk is {milk}\n"
        f"Add-ons: {', '.join(add_ons)}"
    )

    # we can add as many add-ons as we want, including none:
brew_coffee_with_options("Cappuccino", 1, 4,)

#**kwargs means the function accepts any number of optional keyword arguments after the required positional arguments
# they will be stored in a dictionary where the keys are the argument names and the values are the argument values

def brew_coffee_with_options(
        coffee_type,
        *add_ons,
        strength,
        milk,
        **kwargs
):
    print(f"{kwargs=}")
    print(type(kwargs))
    print(
        f"coffee is {coffee_type}\n"
        f"strength is {strength}\n"
        f"milk is {milk}\n"
        f"Add-ons: {', '.join(add_ons)}"
    )
    for key, value in kwargs.items():
        # print(f"\t{key.replace('_', '')}: {value}")
        print(f"\t{key}: {value}")

brew_coffee_with_options(
    "Latte",
    "vanilla syrup",
    strength=3,
    milk=2,
    milk_type="almond milk",
    temperature="extra hot"
)

# we can call **kwards something else, like for example **instructions