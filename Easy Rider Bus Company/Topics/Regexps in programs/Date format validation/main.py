import re

string = input()
reg = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'

print(bool(re.match(reg, string)))
