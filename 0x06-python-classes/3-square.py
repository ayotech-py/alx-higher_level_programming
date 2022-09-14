#!/usr/bin/python3
"""This module returns the area of a square"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initialization"""
        if type(size) != int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this method returns the area"""
        return self.__size * self.__size
