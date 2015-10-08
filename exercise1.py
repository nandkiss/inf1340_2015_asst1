#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


money = 1000.00
print(money)

original_stock_price = 900
subsequent_stock_price = 942.75
commission = 0.03
amount_of_shares_purchased = 2000
amount_of_shares_sold = 2000

initial_investment = original_stock_price * amount_of_shares_purchased
initial_investment = initial_investment - initial_investment * commission
print("Money invested on stock purchase ") + str(initial_investment)


subsequent_investment = subsequent_stock_price * amount_of_shares_sold
subsequent_investment = subsequent_investment - subsequent_investment * commission
print("Money made on stock sale ") + str(subsequent_investment)



final_transaction_amount = subsequent_investment - initial_investment
print("Final transaction amount ") + str(final_transaction_amount)


def calculate_investment (shares, price, commission):
   before_commission = shares * price
   owed_to_broker = before_commission * commission
   total = before_commission - owed_to_broker
   return total

initial_investment = calculate_investment(2000, 900, 0.03)
subsequent_investment = calculate_investment(2000, 942.75, 0.03)

if subsequent_investment < initial_investment:
   print("Lakshmi lost money")
else:
   print("Lakshmi made money")


