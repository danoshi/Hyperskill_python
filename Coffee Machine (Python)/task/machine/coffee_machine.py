# Write your code here
water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def echo() -> None:
    print("The coffee machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee} g of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${money} of money")


def buy() -> None:
    global water, milk, coffee, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    i = input()
    if i == "back":
        return
    elif int(i) == 1 and water >= 250 and coffee >= 16 and cups >= 1:
        water -= 250
        coffee -= 16
        cups -= 1
        money += 4
    elif int(i) == 2 and water >= 350 and coffee >= 20 and cups >= 1 and milk >= 75:
        water -= 350
        milk -= 75
        coffee -= 20
        cups -= 1
        money += 7
    elif int(i) == 3 and water >= 200 and coffee >= 12 and cups >= 1 and milk >= 100:
        water -= 200
        milk -= 100
        coffee -= 12
        cups -= 1
        money += 6
    else:
        print(f"Sorry, not enough resources!")


def fill() -> None:
    global water, milk, coffee, cups
    print("Write how many ml of water you want to add: ")
    w = int(input())
    print("Write how many ml of milk you want to add: ")
    m = int(input())
    print("Write how many grams of coffee beans you want to add: ")
    cof = int(input())
    print("Write how many disposable cups you want to add: ")
    cup = int(input())
    water += w
    milk += m
    coffee += cof
    cups += cup


def take() -> None:
    global money
    print(f"I gave you ${money}")
    money -= money


def main() -> None:
    a = True
    while a:
        print("Write action (buy, fill, take, remaining, exit): ")
        i = input()
        if i == "buy":
            buy()
        elif i == "fill":
            fill()
        elif i == "take":
            take()
        elif i == "remaining":
            echo()
        elif i == "exit":
            a = False


main()
