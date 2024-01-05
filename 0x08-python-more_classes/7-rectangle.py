#!/usr/bin/python3

""" Now for Rectangle on Task 7 """


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Optional width of the rectangle (default is 0).
            height (int): Optional height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Public instance method to calculate the rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method to calculate the rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += str(self.print_symbol) * self.__width + '\n'
            return rectangle_str.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method to print a message when an instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
