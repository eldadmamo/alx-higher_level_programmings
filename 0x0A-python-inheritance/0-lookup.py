#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """
    Returns a list all attributes and methods of object.
    Args:
        obj (any): The object for which we
        want to retrieve attributes and methods.
    Returns:
        list: A list of attributes and methods of object.
    """
    return dir(obj)
