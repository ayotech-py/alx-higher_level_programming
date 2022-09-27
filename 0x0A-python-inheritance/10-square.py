#!/usr/bin/python3
BaseGeometry = __import__("9-rectangle").Rectangle
"""New Square Class"""


class Square(BaseGeometry):
    """This method initializes the class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This method returns area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """This method return a string"""
        return "[{}] {}/{}"\
            .format(self.__class__.__name__, self.__size, self.__size)
