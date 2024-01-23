#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new instance of the Square class."""
        self.size = size
    
    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
