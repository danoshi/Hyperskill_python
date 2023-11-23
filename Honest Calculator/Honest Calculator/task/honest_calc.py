# write your code here
def calculator():
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."

    a = True

    while a:
        print(msg_0)
        calc = str(input())
        x, oper, y = calc.split()

        if x.isalpha() or y.isalpha():
            print(msg_1)

        elif oper not in ('-', '+', '/', '*'):
            print(msg_2)

        elif oper in '+':
            res = float(x) + float(y)
            print(res)
            a = False

        elif oper in '-':
            res = float(x) - float(y)
            print(res)
            a = False

        elif oper in '*':
            res = float(x) * float(y)
            print(res)
            a = False

        elif oper in '/' and int(y) != 0:
            res = float(x) - float(y)
            print(res)
            a = False

        else:
            print(msg_3)


calculator()
