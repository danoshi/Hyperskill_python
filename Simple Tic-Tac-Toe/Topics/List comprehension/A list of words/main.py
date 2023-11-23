# work with the preset variable `words`
#words = ['apple', 'pear', 'banana', 'Ananas']

my_list = [word for word in words if word.startswith('a') or word.startswith('A')]
print(my_list)
