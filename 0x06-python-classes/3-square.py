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
        conductor for our class.
        Args:
            size: square's size in integer
        Return:
            None
        '''
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''
        calculates the area of square
        Args:
            None
        Return:
            squared size
        '''
        return self.__size * self.__size
