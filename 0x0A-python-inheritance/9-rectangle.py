#!/usr/bin/python3
"""New Class that inherits other classes"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Initializes the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This returns the name of the attributes"""
        return "[{}] {}/{}"\
            .format(self.__class__.__name__, self.__width, self.__height)
