import re

string = input()
# your code here
template = r"Good\s(morning|afternoon|evening)"

if re.match(template, string):
    print(re.match(template, string).group())
else:
    print("No greeting!")
