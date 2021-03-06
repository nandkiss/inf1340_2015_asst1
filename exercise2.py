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

    Inputs: 3, 4, 5, 6, 7, 8, 9 or 10

    Expected Outputs: triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Errors: any number < 3 or > 10

    """

    # The program only takes input once and decides which shape it is based on # of sides
    shape = raw_input("Number of sides on shape between 3 and 10: ")
    if shape == ("3"):
        print ("triangle")
    elif shape == ("4"):
        print ("quadrilateral")
    elif shape == ("5"):
        print ("pentagon")
    elif shape == ("6"):
        print ("hexagon")
    elif shape == ("7"):
        print ("heptagon")
    elif shape == ("8"):
        print ("octagon")
    elif shape == ("9"):
        print ("nonagon")
    elif shape == ("10"):
        print ("decagon")
    # the program only chooses shapes between 3-10 sides. Anything else will print 'Error'
    else:
        print ("Error")
# name_that_shape ()