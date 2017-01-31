#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square is subclass from Rectangle
    """
    """
    calling super().__init__() is calling
    Rectangle.__init__
    """
    
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        
        


            
