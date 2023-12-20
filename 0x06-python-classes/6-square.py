#!/usr/bin/python3

""" Square class for working with a square. """


class Square:
    '''
    Defines a square and calculates its area
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        conductor for square class. for Instantiation
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        property getter for the size of the square.
        Return:
            the initial size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Property setter for the size of the square.
        Args:
            value(int): the new square's size.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
        Property getter for the Private instance attribute: `position`
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise IndexError(
                    "position must be a tuple of 2 positive integers")
        for x in value:
            if not isinstance(x, int) or x < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
        calculates the area of square
        Return:
            squared size
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints the square with the character `#` to stdout
        if size is zero, it prints a blank line.
        '''
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            if self.__position[1] > 0:
                print(f" {'#' * self.__size}")
            else:
                print(f"{' ' * self.__position[0]}{'#' * self.__size}")
