# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
my_list = [num for num in my_numbers if num % 2 == 0]
print(my_list)
