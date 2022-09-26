#!/usr/bin/python3
"""Exercise 7"""


class BaseGeometry(object):
    """New Class"""

    def area(self):
        """This method raises an exemption error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validate inputed data"""
        self.name = name
        self.value = value
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
