#!/usr/bin/python3
"""Rectangle Show."""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        """new Rectangle.

        Args:
            width (integer): The width rectangle.
            height (integer): The height rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width integer")
        if value < 0:
            raise ValueError("width must greater than 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("integer height")
        if value < 0:
            raise ValueError("height must greater than 0")
        self.__height = value
