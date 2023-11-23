name = input()

special_char = ['*', '_', '~', '*', '`']

for x in special_char:
    if x in name:
        name = name.strip(x)

print(name)
