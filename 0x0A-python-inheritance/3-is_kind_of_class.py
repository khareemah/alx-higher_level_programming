#!/usr/bin/python3
"""A function that checks inheritance of an object"""


def is_kind_of_class(obj, a_class):
    """checks if object is an instance of a class or inherited class
        Args:
            obj - object to check
            a_class - class to check
    """
    return isinstance(obj, a_class)
