#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    idx_tmp = 0
    for i in my_list:
        if idx_tmp == idx:
            my_list[idx] = element
            return (my_list)
        idx_tmp +=1
