#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class that inherit list object"""


    def print_sorted(self):
        """A function that sorts a list"""
        print(sorted(self))
