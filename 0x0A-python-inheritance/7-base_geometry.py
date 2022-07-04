#!/usr/bin/python3
"""Module that has an empty base class BaseGeometry
"""


class BaseGeometry:
    """Class that defines a shape
    """

    def area(self):
        """function that raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates argument
            Args:
                name - string
                value - integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} mjst be greater than 0")
