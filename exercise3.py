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
    user_input = raw_input ("Is the car silent when you turn the key?")
    # First yes branching
    if user_input == ("Y"):
        user_input = raw_input ("Are the battery terminals corroded?")
        if user_input == ("N"):
            print ("Replace cables and try again.")
        if user_input == ("Y"):
            print ('Clean terminals and try starting again.')
    # First no branching
    # Had to use elif because if it is "if" then it recognized both N and printed both
    elif user_input == ("N"):
        user_input = raw_input ("Does the car make a clicking noise?")
        if user_input == ("Y"):
            print ("Replace the battery.")
        if user_input == ("N"):
            user_input = raw_input ("Does the car crank up but fail to start?")
            # Another section on graph begins
            if user_input == ("Y"):
                print ("Check spark plug connections.")
            if user_input == ("N"):
                user_input = raw_input ("Does the engine start and then die?")
                # Another section on graph begins
                if user_input == ("Y"):
                    user_input = raw_input ("Does your car have fuel injection?")
                    if user_input == ("N"):
                        print ("Check to ensure the choke is opening and closing.")
                    if user_input == "Y":
                        print ("Get it in for service.")
                elif user_input == ("N"):
                    print ("Engine is not getting enough fuel. Clean fuel pump.")

# diagnose_car()

