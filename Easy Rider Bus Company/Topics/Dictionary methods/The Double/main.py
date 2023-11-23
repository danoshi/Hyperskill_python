# put your python code here
from string import ascii_lowercase

double_alphabet = dict.fromkeys(ascii_lowercase, 0)
for single in double_alphabet:
    double_alphabet[single] = single * 2
