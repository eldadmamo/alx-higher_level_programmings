#!/usr/bin/python3
"""class function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object of a given class.
    Args:
        obj: The object to be checked.
        a_class: The class to check .
    Returns:
        True if obj is an instance of class, False otherwise.
    """
    return isinstance(obj, a_class)
