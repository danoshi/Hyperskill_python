from collections import deque

counter = int(input())

my_stack = []
my_second_stack = deque()
count = 0
for _x in range(0, counter):
    actions = input().split(" ", 1)
    if "BUY" in actions:
        count += 1
        my_stack.append(actions[1])

    elif "READ" in actions:
        my_second_stack.append(my_stack[count - 1])
        my_stack.pop()
        count -= 1


for x in range(0, len(my_second_stack)):
    print(my_second_stack[x])
