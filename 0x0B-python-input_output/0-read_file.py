#!/usr/bin/python3
"""file reading"""


def read_file(filename=""):
    """
    Reads contents of a file and prints them to the console.

    Args:
        filename (str, optional): The name of the file to be
        read. 

    Returns:
        None

    Example:
        read_file("example.txt")
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
