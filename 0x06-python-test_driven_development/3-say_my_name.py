#!/usr/bin/python3
"""
The Print Name module.
Example:
>>> say_my_name("Guy", "Guyguy")
My name is Guy Guyguy
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name and last_name must be strings")
    print("My name is {:s} {:s}". format(first_name, last_name))
