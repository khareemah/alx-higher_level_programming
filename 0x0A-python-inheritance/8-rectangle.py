#!/usr/bin/python3
"""Module that holds the class BaseGeometry
"""


class BaseGeometry:
    """Class that defines a shape
    """

    pass

    def area(self):
        """Function that calculates the area of a shapre
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates input
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the subclass
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
