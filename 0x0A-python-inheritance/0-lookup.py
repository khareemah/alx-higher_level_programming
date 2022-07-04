#!/usr/bin/python3
"""A function that looks up method and attributes"""


def lookup(obj):
    """Function tat returns list of methods and attributes
    Args:
    obj - object to check
    """
    return dir(obj)
