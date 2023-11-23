import re

word = input()
# your code here
if bool(re.match('the\Z', word)):
    print("True")
else:
    print("False")
