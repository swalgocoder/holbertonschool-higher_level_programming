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
    for delim in text.strip():
        if delim == '.' or delim == '?' or delim == ':':
            print("{:s}".format(delim), end="")
            print()
            print()
            spc_sym = 1
        else:
            if not spc_sym:
                print("{:s}".format(delim), end="")
            else:
                if delim == ' ' or delim == '\t':
                    continue
                print("{:s}".format(delim), end="")
                spc_sym = 0
