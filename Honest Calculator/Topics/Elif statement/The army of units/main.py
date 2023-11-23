def army():
    arm = int(input())
    if arm < 1:
        print("no army")
    elif 1 <= arm <= 9:
        print("few")
    elif 10 <= arm <= 49:
        print("pack")
    elif 50 <= arm <= 499:
        print("horde")
    elif 500 <= arm <= 999:
        print("swarm")
    elif arm >= 1000:
        print("legion")


army()
