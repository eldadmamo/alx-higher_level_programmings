#!/usr/bin/python3
"""appending file"""


def append_write(filename="", text=""):
    """
    Opens the specified file in append mode.

    Args:
        filename (str, optional): The name of the file.
        text (str, optional): The text written file.

    Returns:
        int: The number of characters
    """
    with open(filename, "+a", encoding='utf-8') as file:
        return file.write(text)
