# put your python code here
word = input()
new_word = word.split()
a = 0
for letters in new_word:
    if "A" in letters:
        a = a + 1
calc = round(a / len(new_word), 2)
print(calc)
