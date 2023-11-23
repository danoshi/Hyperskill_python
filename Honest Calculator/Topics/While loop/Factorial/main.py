#  You can experiment here, it won’t be checked
def calc():
    num = int(input())
    fac = 1
    i = 1

    while i <= num:
        fac = fac * i
        i = i + 1
    print(fac)


calc()
