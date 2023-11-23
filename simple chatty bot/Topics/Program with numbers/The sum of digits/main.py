# put your python code here
num = int(input())
a = 10
last_digit = num % a
first_digit = num // 100
test = num // 10
middle_digit = test % a

print(last_digit + first_digit + middle_digit)
