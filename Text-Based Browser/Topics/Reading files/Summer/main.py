#  write your code here 
file = open('./data/dataset/input.txt', 'r')
count = file.readlines().count('summer\n')


print(count)
