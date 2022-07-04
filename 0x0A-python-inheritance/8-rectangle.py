#!/usr/bin/python3

class BaseGeometry:
    """Class that defines a shape
    """

    def area(self):
        """function that raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates argument"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} mjst be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """initilize instance variable"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
