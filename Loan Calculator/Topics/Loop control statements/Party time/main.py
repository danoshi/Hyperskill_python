count = 0
names = []

while count == 0:
    name = input()
    if name != ".":
        names.append(name)
    elif name == ".":
        print(names)
        print(len(names))
        count = count + 1
