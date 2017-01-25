#!/usr/bin/python3
"""
self.attr = 0: all attributes are accessible to all codes
class Fool: self.__attr = 0, attribute private

"""

class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        
        if type(width) != int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")

        """
        a property to access it
        """
        @property
        def width(self):
            return (self.__width)

        @property
        def height(self):
            return (self.__height)

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if int(value) < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if int(value) < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
