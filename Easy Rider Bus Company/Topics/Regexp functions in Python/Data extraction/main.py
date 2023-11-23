import re

string = input()
# your code
print(re.findall('<START>(.*)<END>', string)[0])
