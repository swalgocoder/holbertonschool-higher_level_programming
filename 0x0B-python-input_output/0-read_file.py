#!/usr/bin/python3
"""
text file (UTF8) read
"""


def read_file(filename=""):
        f = open(filename, 'r')
        print(f.read(), end="")
