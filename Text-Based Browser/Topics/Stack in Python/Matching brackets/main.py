from collections import deque

expression = input()
my_stack = deque()

for e in expression:
    if e == '(':
        my_stack.append(e)
    elif len(my_stack) > 0 and e == ')':
        my_stack.pop()
    elif e == ')':
        my_stack.append(e)

if len(my_stack) == 0:
    print("OK")
else:
    print("ERROR")
