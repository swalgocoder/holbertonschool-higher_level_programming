#!/usr/bin/python3
"""

"""


def number_of_lines(filename=""):
        with open(filename, 'r') as f:
            line = '\n'
            return(f.read().count(line))
