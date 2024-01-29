#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Define  rectangle."""

    def __init__(self, width=0, height=0):
        """Shows a new Rectangle.

        Args:
            width (integer): widthrectangle.
            height (integer): height rectangle.
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
            raise TypeError(" integer")
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

    def __str__(self):
        """Print Rectangle.

        Rectangle # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
