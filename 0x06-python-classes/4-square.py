#!/usr/bin/python3
"""defines a class called Square"""


class Square:

    """Represents a square"""

    def __init__(self, size=0):

        """Initializes the data
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):

        """Retrieves the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value
        Args:
            value: the size of the square
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
#            raise TypeError("size must be an integer")

    def area(self):

        """returns area of a square"""

        return (self.__size * self.__size)
