#!/usr/bin/python3

""" an empty Rectangle class """


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Optional width of the rectangle (default is 0).
            height (int): Optional height of the rectangle (default is 0).
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

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
