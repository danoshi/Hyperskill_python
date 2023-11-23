import itertools

# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
#
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
#
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]
#

eating = itertools.product(main_courses, desserts, drinks)
price = itertools.product(price_main_courses, price_desserts, price_drinks)
for meal, price in zip(eating, price):
    if sum(price) <= 30:
        print(*meal, sum(price))
