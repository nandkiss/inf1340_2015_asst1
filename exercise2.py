#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("Error")

shape = raw_input ("Number of sides on shape between 3 and 10: ")
if shape == ("3"):
    print ("Triangle")
elif shape == ("4"):
    print ("Quadrilateral")
elif shape == ("5"):
    print ("Pentagon")
elif shape == ("6"):
    print ("Hexagon")
elif shape == ("7"):
    print ("Heptagon")
elif shape == ("8"):
    print ("Octagon")
elif shape == ("9"):
    print ("Nonagon")
elif shape == ("10"):
    print ("Decagon")
else:
    print ("Error")
name_that_shape