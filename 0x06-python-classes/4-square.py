#!/usr/bin/python3

""" Square class for area"""


class Square:
    '''
    Defines a square and calculates its area
    '''

    def __init__(self, size=0):
        '''
        conductor for square class.
        '''
        self.__size = size

    @property
    def size(self):
        '''
        property getter for the size of the square.
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
        Return:
            squared size
        '''
        return self.__size ** 2
