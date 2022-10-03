#!/usr/bin/python3
"""New file in a package"""


class Base:
    """New Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
