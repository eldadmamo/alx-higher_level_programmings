#!/usr/bin/python3
"""this is file writing"""


def write_file(filename="", text=""):
    """
    text to the file with the given filename.

    :param filename: a string representing the name of
    the file to be. If not empty string is used as
    the default value.
    :param text: string representing the text to be
    written to the file. If not , an empty string is used as
    the default value.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
