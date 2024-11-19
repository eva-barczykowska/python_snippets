def how_many_light_sabers_do_you_own(name=""):
    return 18 if name == "Zach" else 0


print(how_many_light_sabers_do_you_own("Zach"))  # , 18)
print(how_many_light_sabers_do_you_own())  # , 0)
print(how_many_light_sabers_do_you_own("zach"))  # , 0)


def how_many_light_sabers_do_you_own(name=""):
    if name == "Zach":
        return 18
    else:
        return 0
    

print(how_many_light_sabers_do_you_own("Zach"))  # , 18)
print(how_many_light_sabers_do_you_own())  # , 0)
print(how_many_light_sabers_do_you_own("zach"))  # , 0)
