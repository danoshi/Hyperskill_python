import re

name = input()
template = r"\D\w"

if re.match(template, name):
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
