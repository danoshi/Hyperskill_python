import re

string = input()
# your code here
pattern = r'ou'
word = re.compile(pattern)
sub_word = re.sub(word, 'o', string)
print(sub_word)
