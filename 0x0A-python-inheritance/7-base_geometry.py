#!/usr/bin/python3


class BaseGeometry:
    def area(self):
        """
        public instance of area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <=0:
            raise ValueError('{} must be greater than 0'.format(name))
            
