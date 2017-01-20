#!/usr/bin/python3
"""
The function text_indentation()
that prints a text with 2 new lines after each characters: ., ? and :.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spc_sym = 0
    for line in text.strip():
        if line == '.' or line == '?' or line == ':':
            print("{:s}".format(line), end="")
            print()
            print()
            spc_sym = 1
        else:
            if not spc_sym:
                print("{:s}".format(line), end="")
            else:
                if line == ' ' or line == '\t':
                    continue
                print("{:s}".format(line), end="")
                spc_sym = 0
