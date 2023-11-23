import re

string = input()
# your code here
pattern = r'(?<=-).*'
result = re.search(pattern, string)
print(result.group())
