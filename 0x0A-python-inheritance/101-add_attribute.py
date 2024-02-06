#!/usr/bin/python3
"""add new attribute"""


def add_attribute(obj, att, value):
    """add attribute
    Args:
        obj (_type_): description
        att (_type_): description
        value (_type_): description
    Raises:
        TypeError: _description_
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
