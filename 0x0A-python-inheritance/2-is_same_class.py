#!/usr/bin/python3
"""class and obj
"""


def is_same_class(obj, a_class):
    """
    Check if an object is of a specific class.
    Args:
        obj: The object to be checked.
        a_class: The class to compare the object.
    Returns:
        True if obj is an instance class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
