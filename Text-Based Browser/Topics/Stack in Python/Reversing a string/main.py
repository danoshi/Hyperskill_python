from collections import deque

n = int(input())

my_stack = deque()

for _ in range(0, n):
    action = input()
    my_stack.append(action)

for x in range(0, len(my_stack)):
    print(my_stack.pop())
