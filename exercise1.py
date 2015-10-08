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

#I have defined the following variables because we require them to solve this problem
original_stock_price = 900
subsequent_stock_price = 942.75
commission = 0.03
amount_of_shares_purchased = 2000
amount_of_shares_sold = 2000

initial_investment = original_stock_price * amount_of_shares_purchased
#This gives us the amount Lakshmi spent on her initial investment before paying her broker
initial_investment = initial_investment - initial_investment * commission
#Now, we have the amount that she invested after paying her broker
print("Money invested on stock purchase ") + str(initial_investment)
#I added the string so that it is clear that this value shows the money she invested on the stock purchase


subsequent_investment = subsequent_stock_price * amount_of_shares_sold
#This gives us the amount Lakshmi made by selling her stock before paying her broker
subsequent_investment = subsequent_investment - subsequent_investment * commission
#Now, we have the amount that she made after paying her broker
print("Money made on stock sale ") + str(subsequent_investment)


#In order to find out whether Lakshmi made money on this transaction, we calculate
# the difference between the initial and subsequent transactions
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


