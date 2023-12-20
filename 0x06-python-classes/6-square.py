#!/usr/bin/python3

""" Square class for working with a square. """


class Square:
    '''
    Defines a square and calculates its area
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Constructor for Square class.

        Args:
            size (int): The size of the square, must be a non-negative integer.
            position (tuple): The (x, y) position of the square, must be non-negative integers.

        Raises:
            TypeError: If size or position are not integers or if position is not a tuple.
            ValueError: If size or position values are negative.
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
        Return:
            initial position tuple.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Property setter for the position to place the square.
        Args:
            value(tuple): with exactly two elements set the position.
        Raises:
            IndexError: If value has more than two elements.
            TypeError: If value's element is not a positive integer.
        '''
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
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(f"{' ' * self.__position[0]}{'#' * self.__size}")
