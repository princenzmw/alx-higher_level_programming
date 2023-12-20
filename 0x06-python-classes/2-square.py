#!/usr/bin/python3

""" square class"""


class Square:
    """ It defines a square
        Attributes:
            size (int): the size for square

        methods:
            None
    """

    def __init__(self, size=0):
        """
        Initialize the size of the square
        Args:
            size
        Return:
            None
        """
        self.__size = size
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
