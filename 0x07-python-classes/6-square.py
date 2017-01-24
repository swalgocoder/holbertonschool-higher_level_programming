#!/usr/bin/python3
"""
The Square Class creates a Square object with initialized "size"
which is private attribute
"""


class Square:

    def __init__(self, size = 0, position = (0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ 
        retrieves position 
        """
        return self.__position

    def position(self, value):
        """
        - sets position
        - raise errors checking
        """
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0 is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ 
        returns the current square area 
        """
        return self.__size * self.__size

    def my_print(self):
        """ 
        prints in stdout the square with the character # 
        """
        size = self.size
        pos = self.position
        if size == 0:
            print("")
        for p1 in range(pos[1]):
            print(" ")
        for i in range(size):
            for p2 in range(pos[0]):
                print("", end=" ")
            for j in range(size):
                print("#", end="")
            print("")
