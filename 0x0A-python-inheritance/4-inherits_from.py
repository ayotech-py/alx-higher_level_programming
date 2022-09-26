#!/usr/bin/python3
"""Exercise 4"""


def inherits_from(obj, a_class):
    """This function returns true of obj is an instance
    of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
