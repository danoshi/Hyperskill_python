# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
passwords.sort(key=len)
for p in passwords:
    value = len(p)
    print(f"{p} {value}")
