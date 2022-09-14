#!/usr/bin/python3
"""This module returns the area of a square"""


class Square:
    """this is the square class"""
    def __init__(self, size=0):
        """initialization"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be <= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be <= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
