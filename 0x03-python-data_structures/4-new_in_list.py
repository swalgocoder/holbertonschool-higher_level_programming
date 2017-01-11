#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    my_list2 = my_list[:]
    idx_tmp = 0
    for i in my_list2:
        if idx_tmp == idx:
            my_list2[idx_tmp] = element
            return (my_list2)
        idx_tmp += 1
