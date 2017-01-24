#!/usr/bin/python3
"""
The Square Class creates a Square object with initialized "size"
which is private attribute
"""


class Square:
    """
    size initialized with 0, error checking
    """
    def __init__(self, size = 0):
        """
        The __init__ method
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be positive")
        self.__size = size
	


