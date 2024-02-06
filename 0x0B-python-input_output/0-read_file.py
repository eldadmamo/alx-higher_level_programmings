#!/usr/bin/python3
"""file reading"""


def read_file(filename=""):
    """
    Reads the contents file and prints.

    Args:
        filename (str, optional): The name of the file 
        read. If no filename is provided, an empty string 

    Returns:
        None

    Example:
        read_file("example.txt")

    This code read contents of the file named "example.txt"
    and print .
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
