# Emptiness
# this
items = []
if not items:
    print("No items were found")

# Instead of this:

if len(items) == 0:
    print("No items were found")

# Boolean checking

# I
# prefer
# this:
user = "Ewan"
if not user.is_admin:
    print("Not an admin")

# Instead
# of
# this:
user = "Ewa"
if user.is_admin == False:
    print("Not an admin")

# None
# checking

# I
# often
# prefer
# this:

if user:
    print("We have a user now")

# Over
# this:

if user is not None:
    print("We have a user now")

# Unless user could reasonably be falsey butnot None(an empty string for example)
# and we really needed to check for None versus not -None rather than falsey versus truthy.

# Zero and non - zero
# checking

# But
# I
# do
# not prefer
# this:
n = 99
if n % 2:
    print("n is odd")

# Instead, I
# prefer
# this:

if n % 2 != 0:  #  potentially more readable
    print("n is odd")

# Though
# I
# do
# sometimes
# go
# against
# my
# own
# preference
# here.
#
# Sometimes
# instead
# of
# this:
matched = 0  # count of matches
if matched == 0:
    print("No matches")

# I'll write this:

if not matched:
    print("No matches")

"""While I am using truthiness
for a zero - check in that last example, it('s specifically checking the value of a single variable'
'(not an expression, like n % 2) and it')s exclusively in the context of an integer-based count."""