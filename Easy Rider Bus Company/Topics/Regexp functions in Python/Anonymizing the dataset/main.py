import re

string = input()
# your code
template = r'@([A-Za-z0-9_]+)'
template2 = r'@([A-Za-z0-9_]+)'
replacement = '<AUTHOR>'
replacement2 = "<HANDLE>"

res1 = re.sub(template, replacement, string, count=1)
res2 = re.sub(template2, replacement2, res1)
print(res2)
