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

    def area(self):
        """Returns the area for a rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """Returns a defined rectangle description
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Class that inherits from Rectangle but makes a square
    """

    def __init__(self, size):
        """Initializes a square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
