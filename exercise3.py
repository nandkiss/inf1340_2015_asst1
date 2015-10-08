#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("The battery cables may be damaged. Replace cables and try again.")
diagnose_car()

user_input = raw_input ("Is the car silent when you turn the key?: ")
if user_input == ("y"):
    user_input = raw_input ("are the battery terminals corroded?: ")
    if user_input == ("y"):
        print ("Clean terminals and try starting again.")
    if user_input == ("n"):
        print ("Replace cables and try again.")
if user_input == ("n"):
    user_input = raw_input ("Does the car make a clicking noise?: ")
    if user_input == ("y"):
        print ("Replace the battery.")
    if user_input == ("n"):
        user_input = raw_input ("Does the car crank up but fail to start?: ")
        if user_input == ("y"):
            print ("Check spark plug connections.")
        if user_input == ("n"):
            user_input == raw_input ("Does the engine start and then die?: ")
            if user_input == ("y"):
                user_input = raw_input ("Does your car have fuel injection?: ")
                if user_input == ("n"):
                    print ("Check to ensure the choke is opening and closing.")
                if user_input == ("y"):
                    print ("Get it in for service.")



