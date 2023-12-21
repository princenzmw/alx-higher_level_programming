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
            position (tuple): The (x, y) position of the square,
            must be non-negative integers.

        Raises:
            TypeError: If size or position are not integers or if
                position is not a tuple.
            ValueError: If size or position values are negative.
        '''
        self.__size = size
        self.__position = position

    def __str__(self):
        """Show Python how to print the square my way"""
        return self.print_positiont()[:-1]

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
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''
        calculates the area of square
        Return:
            squared size
        '''
        return self.__size ** 2

    def print_position(self):
        """ return spaces of the position. """

        postn = ""
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            postn += "\n"
        for _ in range(self.size):
            for _ in range(self.position[0]):
                postn += " "
            for _ in range(self.size):
                postn += "#"
            postn += "\n"
        return postn

    def my_print(self):
        """print the square in position"""
        print(self.print_position(), end='')
