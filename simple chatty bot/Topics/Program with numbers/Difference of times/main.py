# put your python code here
a = 3600
b = 60

num_1 = int(input()) * a
num_2 = int(input()) * b
num_3 = int(input())

num_4 = int(input()) * a
num_5 = int(input()) * b
num_6 = int(input())

erg_1 = (num_1 + num_2 + num_3)
erg_2 = (num_4 + num_5 + num_6)
erg_final = abs(erg_1 - erg_2)

print(erg_final)
