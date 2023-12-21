class Square:
    """Class that defines a square."""

    def __init__(self, size: int = 0):
        """Initialize the size of the square.

        Args:
            size (int): The size of the square, must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self) -> int:
        """Property getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Property setter for the size of the square.

        Args:
            value (int): The new size of the square, must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

# Example usage:
try:
    square = Square(5)
    print(square.area())  # Output: 25
except Exception as e:
    print(e)

print("-" * 16)

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
