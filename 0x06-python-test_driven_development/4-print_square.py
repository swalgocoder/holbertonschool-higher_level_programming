#!/usr/bin/python3
"""
function print_square()
that prints a square with the character #.
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print()
