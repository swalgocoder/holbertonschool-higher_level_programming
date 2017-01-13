#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp_dict = []
    for my_key, my_value in my_dict.items():
        if my_value is value:
            tmp_dict.append(my_key)
    for item in tmp_dict:
        del my_dict[item]
    return(my_dict)
