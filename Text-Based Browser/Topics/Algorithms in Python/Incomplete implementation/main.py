def startswith_capital_counter(names):
    counter = 0
    for name in names:
        for n in name:
            if n.isupper():
                counter += 1
    return counter

