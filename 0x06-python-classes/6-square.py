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
    @property
    def position(self):

        """ retrieves position """

        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size value
        Args:
            value: the size of the square
        """

        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Sets the position value
        Args:
            value: the position
        """
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """returns area of a square"""

        return (self.__size * self.__size)

    def my_print(self):

        """ prints square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format("#"), end="")
                print()
