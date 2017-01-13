#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, v in enumerate(new_list):
        if v == search:
            new_list.pop(i)
            new_list.insert(i, replace)
    return new_list
