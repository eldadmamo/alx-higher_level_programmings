#!/usr/bin/python3
"""Show a Rectangle class."""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        """begin a new Rectangle.

        Args:
            width (integer): The width rectangle.
            height (integer): The height rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("integer width")
        if value < 0:
            raise ValueError("width greater than 0")
        self.__width = value

    @property
    def height(self):
        """height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("integer height")
        if value < 0:
            raise ValueError("height greater than 0")
        self.__height = value

    def area(self):
        """Return Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
