#!/usr/bin/python3
"""
write (append) a string to a file
"""


def append_write(filename="", text=""):
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(text)
        return len([char for char in text])
