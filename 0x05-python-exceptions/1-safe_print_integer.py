#!/usr/bin/python3

def safe_print_integer(value):
    """dislay value with "{:d}".format().

    Args:
        int: The integer to print.

    Returns:
        If a Error occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
