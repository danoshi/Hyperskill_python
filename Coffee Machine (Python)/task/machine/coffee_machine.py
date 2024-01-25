# Write your code here

def water(cups: int) -> int:
    return int(cups / 200)


def milk(cups: int) -> int:
    return int(cups / 50)


def beans(cups: int) -> int:
    return int(cups / 15)


def coffee() -> None:
    cup = []
    print("Write how many cups of coffee you will need:")
    w = int(input())
    cup.append(water(w))
    print("Write how many ml of milk the coffee machine has:")
    m = int(input())
    cup.append(milk(m))
    print("Write how many grams of coffee beans the coffee machine has:")
    b = int(input())
    cup.append(beans(b))
    print("Write how many cups of coffee you will need:")
    a = int(input())
    cups = min(cup)
    if a == cups:
        print("Yes, I can make that amount of coffee")
    elif a < cups:
        cups = cups - a
        print(f"Yes, I can make that amount of coffee (and even {cups} more than that)")
    elif a > cups:
        print(f"No, I can make only {cups} cups of coffee")


coffee()
