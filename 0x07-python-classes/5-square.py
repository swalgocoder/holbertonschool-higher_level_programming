#!/usr/bin/python3
"""
The Square Class creates a Square object with initialized "size"
which is private attribute
"""


class Square:

    def __init__(self, size = 0):
        self.size = size

        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >=0")
        self.__size = size
        
    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end = "")
            print()
