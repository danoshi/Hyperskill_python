# put your python code here
number = int(input())
calculation = number % 4 == 0
calculation2 = number % 100 != 0
calculation3 = number % 400 == 0
if calculation and calculation2 or calculation3:
    print("Leap")
else:
    print("Ordinary")
