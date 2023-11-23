def check_email(string):
    if "@" in string and "." in string:
        b = string.index("@")
        a = string.rindex(".")
        if " " not in string and "@." not in string and "." in string\
                and not string.endswith(".") and not string.startswith(".")\
                and a > b and "," not in string:
            return True
        return False
    else:
        return False



