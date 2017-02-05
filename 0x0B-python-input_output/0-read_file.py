#!/usr/bin/python3
"""
text file (UTF8) read
"""


def read_file(filename=""):
        with open(filename, 'r') as f:
            print(f.read(), end="")
