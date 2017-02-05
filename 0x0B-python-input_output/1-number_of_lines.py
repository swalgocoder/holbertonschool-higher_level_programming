#!/usr/bin/python3
"""

"""


def number_of_lines(filename=""):
        f = open(filename, 'r')
        line = '\n'
        return(f.read().count(line))
