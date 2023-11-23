# put your python code here
count = 0
num = []

while count == 0:
    number = int(input())
    if 10 <= number <= 100:
        num.append(number)
    elif number > 100:
        for nums in num:
            print(nums)
        count = count + 1
