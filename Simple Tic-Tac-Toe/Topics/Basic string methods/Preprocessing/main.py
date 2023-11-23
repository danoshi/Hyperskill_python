name = input()

delete = [',', '.', '!', '?']

for x in delete:
    if x in name:
        name = name.replace(x, "")
        name = name.lower()
    else:
        name = name.lower()
print(name)
