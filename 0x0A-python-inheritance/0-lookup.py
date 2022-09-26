#!/usr/bin/python3
"""Returns list of attributes and methods"""


def lookup(obj):
    """This function returns a list of all attributes and
methods of an object"""

    return list(dir(obj))
