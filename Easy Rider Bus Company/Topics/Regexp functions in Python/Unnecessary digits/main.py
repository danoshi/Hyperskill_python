import re       
names = input()
# your code here
template = r"[0-9]+"
res = re.split(template, names)

print(res)
