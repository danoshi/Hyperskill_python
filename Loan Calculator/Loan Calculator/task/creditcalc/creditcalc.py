from math import ceil
from math import log
from math import floor
import argparse


def check_positive_int(value):
    value = int(value)
    if value <= 0:
        print("Incorrect parameters")
        exit()
    return value


def check_positive_float(value):
    value = float(value)
    if value <= 0:
        print("Incorrect parameters")
        exit()
    return value


parser = argparse.ArgumentParser(description="This program prints Differentiate payment options")
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="You need to choose only one option from the list.")
parser.add_argument("--principal", type=check_positive_int, help="This is an integer number.")
parser.add_argument("--interest", type=check_positive_float, help="This is an integer number.")
parser.add_argument("--payment", type=check_positive_int, help="This is an integer number.")
parser.add_argument("--periods", type=check_positive_int, help="This is an integer number.")

args = parser.parse_args()


def calc():
    if args.type == "annuity":
        if args.principal is not None and args.payment is not None and args.interest is not None:
            erg, overpay = num_of_month(args.payment, args.principal, args.interest)
            years, months = year_calc(erg)

            if months > 0:
                print(f'It will take {years} years and {months} months to repay this loan!')
                print(f'Overpayment = {overpay}')
            else:
                print(f'It will take {years} years to repay this loan!')
                print(f'Overpayment = {overpay}')
        elif args.payment is not None and args.periods is not None and args.interest is not None:
            erg, over_pay = loan_principal_func(args.payment, args.periods, args.interest)
            print(f'Your loan principal = {erg}!')
            print(f'Overpayment = {over_pay}')
        elif args.principal is not None and args.periods is not None and args.interest is not None:
            x, overpay = month_payment_(args.principal, args.periods, args.interest)
            print(f'Your annuity payment = {x}!')
            print(f'Overpayment = {overpay}')
        else:
            print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal is not None and args.periods is not None and args.interest is not None:
            erg = diff_pay(args.principal, args.periods, args.interest)
            print(f'Overpayment = {erg}')
        else:
            print("Incorrect parameters")


def diff_pay(loan_principal_, periods, int_rate):
    i = interest_rate(int_rate)
    per = periods + 1
    zw_erg = 0
    for x in range(1, per):
        erg = (loan_principal_ / periods) + i * (loan_principal_ - (loan_principal_ * (x - 1) / periods))
        print(f'Month {x}: payment is {ceil(erg)}')
        zw_erg = zw_erg + ceil(erg)
    end_erg = zw_erg - loan_principal_
    return ceil(end_erg)


def calc_month(principal, months):
    erg = principal / months
    return erg


def loan_principal_func(annuity_payment_, periods, int_rate):
    i = interest_rate(int_rate)
    zw_erg_ = (i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)
    loan_principal_ = ceil(annuity_payment_ / zw_erg_)
    over_pay = (annuity_payment_ * periods) - loan_principal_
    return loan_principal_, over_pay


def month_payment_(loan_principal_, periods, int_rate):
    i = interest_rate(int_rate)
    month_payment = ceil(loan_principal_ * (i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
    zw_erg = (month_payment * periods) - loan_principal_
    return month_payment, zw_erg


def interest_rate(int_rate):
    i = int_rate / (12 * 100)
    return i


def num_of_month(month_pay, loan_prin, int_rate):
    i = interest_rate(int_rate)
    n = ceil(log(month_pay / (month_pay - (i * loan_prin)), 1 + i))
    overpay = (month_pay * n) - loan_prin
    return n, overpay


def year_calc(month):
    year = floor(month / 12)
    rest_month = (month % 12)
    return year, rest_month


calc()
