#!/usr/bin/python3

"""Module of Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Constructs new square.

        Args:
        size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of square."""
        return (self.__size * self.__size)
