# read sums.txt
file = open('sums.txt', 'r')

for num in file:
    n = num.split()
    answer = int(n[0]) + int(n[1])
    print(answer)

file.close()
