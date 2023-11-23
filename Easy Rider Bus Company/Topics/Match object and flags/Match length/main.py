import re

template = r'are you ready??.?.?'
user = input()

if re.match(template, user):
    print(len(re.match(template, user).group()))
else:
    print(0)
