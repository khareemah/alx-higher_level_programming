#!/usr/bin/python3
"""Module that has an empty base class BaseGeometry
"""


class BaseGeometry:
    """Class that defines a shape
    """

    def area(self):
        """function that raise exception"""

        raise Exception("area() is not implemented")
