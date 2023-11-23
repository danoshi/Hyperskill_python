import re

# your code here
name = input()
template = '[B-N][a, e, i, o, u]'

if bool(re.match(template, name)):
    print('Suitable!')
