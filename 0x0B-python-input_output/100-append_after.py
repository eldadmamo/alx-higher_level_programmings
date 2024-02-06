#!/usr/bin/python3
"""text file function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each string file.

    Args:
        filename (str): Name of the file.
        search_string (str): string to search file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
