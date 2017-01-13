#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if not my_dict:
        return None
    if key in my_dict:
        del my_dict[key]
    return (my_dict)
