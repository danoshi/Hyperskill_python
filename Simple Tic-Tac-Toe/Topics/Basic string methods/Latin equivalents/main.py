name = input()


def normalize(name):
    # put your code here
    new_name = name.replace('é', 'e')
    new_name = new_name.replace('ë', 'e')
    new_name = new_name.replace('á', 'a')
    new_name = new_name.replace('å', 'a')
    new_name = new_name.replace('œ', 'oe')
    return new_name.replace('æ', 'ae')

print(normalize(name))
