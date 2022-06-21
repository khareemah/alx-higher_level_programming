#!/usr/bin/python3

"""define a class Square"""


class Square:

    """represent a square"""
    def __init__(self, size=0):

        """initialize instance data
            Args:
                size(int): size of the squarr
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("Size must be an integer")
