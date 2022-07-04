#!/usr/bin/python3
"""A function that checks instance of a specified class"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of a class
        Args:
            obj - object to check
            a_class - class to look
    """
    return type(obj) is a_class
