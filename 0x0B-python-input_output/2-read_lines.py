#!/usr/bin/python3
"""

"""


def read_lines(filename="", nb_lines=0):
        f = open(filename, 'r')
        line = '\n'
        if nb_lines <= 0 or nb_lines >= f.read().count(line):
                print(f.read(), end="")
        else:
                f.seek(0)
                lines = 1
                while lines <= nb_lines: 
                        print(f.readline(), end="") 
                        lines += 1
