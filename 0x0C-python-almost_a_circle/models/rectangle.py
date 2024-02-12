#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init width heigth """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter property """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter property """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter property """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter property """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        ''' area of this rectangle.'''
        return self.width * self.height

    def display(self):
        ''' Prints string rectangle '''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')
