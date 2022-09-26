#!/usr/bin/python3
"""This file contains isinstance"""


def is_same_class(obj, a_class):
    """This function returns true if obj is an 
instance of a_class otherwise false"""

    return (type(obj) == a_class)
