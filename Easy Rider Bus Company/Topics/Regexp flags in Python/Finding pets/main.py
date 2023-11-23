import re 

pets = input()
pattern = r'(dog|cat|parrot|hamster)'
result = re.findall(pattern, pets, flags=re.IGNORECASE)

print(result)
