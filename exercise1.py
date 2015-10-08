#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def calculate_investment (shares, price, commission):
   before_commission = shares * price
   owed_to_broker = before_commission * commission
   total = before_commission - owed_to_broker
   return total

# Plug in the values for shares, price and commission for her initial investment and her subsequent investment
initial_investment = calculate_investment(2000, 900, 0.03)
subsequent_investment = calculate_investment(2000, 942.75, 0.03)

transaction_difference = subsequent_investment - initial_investment

# We added the string to indicate what this value represents. In order to do this, we changed transaction_difference
# from an integer into a string.
print("Money remaining after transaction " + str(transaction_difference))

# If the transaction difference is greater than 1, it implies that she made money. If it is less than 1 (and therefore
# a negative amount), it implies that she lost money.
if transaction_difference > 1:
    print("Lakshmi made money")
else:
    print("Lakshmi lost money")