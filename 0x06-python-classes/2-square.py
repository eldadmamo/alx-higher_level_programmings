#!/usr/bin/python3

"""Display a class Square."""


class Square:
    """Show a square."""

    def __init__(self, size=0):
        """Declare a new Square.

        Args:
            size: size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
