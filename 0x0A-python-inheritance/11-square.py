#!/usr/bin/python3
"""New class"""
BaseGeometry = __import__("9-rectangle").Rectangle


class Square(BaseGeometry):
    """Square Class"""

    def __init__(self, size):
        """initizing the class"""
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """This method returns the square"""
        return self.__width * self.__height

    def __str__(self):
        """This method returns a string"""
        return "[{}] {}/{}"\
            .format(self.__class__.__name__, self.__width, self.__height)
