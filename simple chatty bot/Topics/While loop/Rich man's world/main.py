percentages = 7.1
deposit = int(input())

minimum = 50000
maximum = 700000

i = 0

while minimum < deposit < maximum:
    new_deposit = deposit * percentages / 100
    deposit += new_deposit
    i += 1
print(i)
