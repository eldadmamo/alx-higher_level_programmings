#!/usr/bin/python3
"""inheritance from base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle and provides functionalities
    for the width and height of the rectangle
    and to be sure that they are integers.
    Example Usage:
    rectangle = Rectangle(5, 10)
    """

    def __init__(self, width, height):
        """
        Rectangle object with the given width and height.
        Args:
        width (int):width of the rectangle.
        height (int): height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate area of the rectangle.
        Returns:
            int: area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
