#!/usr/bin/python3
"""
testing adding two arguments,raising errors if their data types are not floats or ints.
"""


def add_integer(a, b):
    """
    Raise TypeError if a or b fails boolean test:
    Raise TypeError for every case that is not either an integer or a float.
    Float gets converted to an int.
    """
    if ((isinstance(a, (int, float))) and isinstance(b, (int, float))):
        a = int(a)
        b = int(b)
        return a + b
    if (isinstance(a, (int, float)) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
