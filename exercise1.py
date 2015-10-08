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

initial_investment = calculate_investment(2000, 900, 0.03)
subsequent_investment = calculate_investment(2000, 942.75, 0.03)
transaction_difference = subsequent_investment - initial_investment

print("Money spent on purchased stocks " + str(initial_investment))
print("Money made on sold stocks " + str(subsequent_investment))
print("Money remaining after transaction " + str(transaction_difference))

if transaction_difference > 1:
    print("Lakshmi made money")
else:
    print("Lakshmi lost money")