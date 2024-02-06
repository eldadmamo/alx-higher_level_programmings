#!/usr/bin/python3
"""square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    Inherits Rectangle class and adds functionality
    specific to squares.
    Attributes:
        __size (int): size of the square.
    Methods:
        __init__(self, size): Square object with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Square object with the given size.
        Args:
            size (int): size of the square.
        Raises:
            ValueError: size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
