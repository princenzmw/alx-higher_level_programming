#!/usr/bin/python3

""" an empty Rectangle class """


class Rectangle:
    """ Defining a rectangle """

    def __init__(self, width=0, height=0):
        """ class constructor """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ property to reteieve width """

        return self.__width

    @width.setter
    def width(self, value):
        """ property setter for the height """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ property to reteieve height """

        return self.__height

    @height.setter
    def height(self, value):

        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
