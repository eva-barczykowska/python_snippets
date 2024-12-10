speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

# Bonus question: Yes, we need the parentheses. Since and has a higher operator precedence than or, so:
(braking_force < acceleration and speed > 0) or acceleration > 0

# Note that removing the parentheses will still print True. However, we still need the parentheses
# for different values for speed, acceleration, and braking_force. For instance:

speed = 0
acceleration = 24
braking_force = 39
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)              # False

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)              # True

# Here, the output changes when we remove the parentheses.
#
# Discussion
# The provided code uses the logical or operator or, which checks whether at least one of its operands is truthy, and the logical and operator and, which checks whether both its operands are truthy.
#
# In the above code, the operands are comparisons with the following values:

braking_force < acceleration  # True
speed > 0                     # False
acceleration > 0              # True

# Therefore, our logical expression breaks down to True and (False or True).
# Since False or True evaluates as True and True and True evaluates as True as well, the value of is_moving is True.