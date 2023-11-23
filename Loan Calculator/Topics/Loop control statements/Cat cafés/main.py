count = 0
number = []
names = []

while count == 0:
    cafe = input()
    if cafe != 'MEOW':
        num = cafe.split()[1]
        name = cafe.split()[0]
        names.append(name)
        number.append(int(num))
    elif cafe == "MEOW":
        max_value = max(number)
        max_index = number.index(max_value)
        print(names[max_index])
        count = count + 1




