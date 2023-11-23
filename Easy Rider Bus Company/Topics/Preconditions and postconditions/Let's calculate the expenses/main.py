import re

string = input().split(',')
# your code here
l = []
erg = 0
pattern = r'(?<=\$)\d+'
for a in string:
    result = re.search(pattern, a)
    if result:
        l.append(result.group())
for i in l:
    erg = erg + int(i)
print(f"This week you have spent: {erg} dollars")

