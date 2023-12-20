#!/usr/bin/python3

""" Square class for area"""


class Square:
    '''
    Defines a square and calculates its area
    Attributes:
        size(int): size must be an integer greater than zero
    Methods:
        area: calculates the area based on size
    '''

    def __init__(self, size=0):
        '''
        conductor for square class.
        Args:
            None
        Return:
            None
        '''
        self.__size = size

    @property
    def size(self):
        '''
        property getter for the size of the square.
        Args:
            None
        Return:
            size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Property setter for the size of the square.
        Args:
            value(int): the new square's size.
        Return:
            None
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        calculates the area of square
        Args:
            None
        Return:
            squared size
        '''
        return self.__size ** 2
