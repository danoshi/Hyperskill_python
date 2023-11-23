lowest_income = 15527
middle_income = 42707
higher_income = 132406

middle_tax = 15
higher_tax = 25
richest_tax = 28


def tax():
    salary = int(input())
    if salary <= lowest_income:
        print(f'The tax for {salary} is 0%. That is 0 dollars!')
    elif lowest_income < salary <= middle_income:
        calculated_tax = calc(salary, middle_tax)
        print(f'The tax for {salary} is {middle_tax}%. That is {calculated_tax:.0f} dollars!')
    elif middle_income < salary <= higher_income:
        calculated_tax = calc(salary, higher_tax)
        print(f'The tax for {salary} is {higher_tax}%. That is {calculated_tax:.0f} dollars!')
    else:
        calculated_tax = calc(salary, richest_tax)
        print(f'The tax for {salary} is {richest_tax}%. That is {calculated_tax:.0f} dollars!')


def calc(income, tax):
    calculated_tax = (income / 100) * tax
    return calculated_tax


tax()
