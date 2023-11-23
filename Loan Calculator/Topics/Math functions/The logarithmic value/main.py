from math import log

num = int(input())
num2 = int(input())

if num2 == 0 or num2 == 1 or num2 < 0:
    print(round(log(num), 2))
else:
    print(round(log(num, num2), 2))
