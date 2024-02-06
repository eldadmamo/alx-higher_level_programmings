#!/usr/bin/python3
"""geometry"""


class BaseGeometry():
    """
    base class other geometry classes.
    Methods:
    - area(): Raises an exception indicating that it is not implemented.
    """

    def area(self):
        """
        Raises:
            Exception: method is not implemented.
        calculate the area of the specific geometry.
        """
        raise Exception("area() is not implemented")
