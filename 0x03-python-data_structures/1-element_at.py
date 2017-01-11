#!/usr/bin/python3
def element_at(my_list, idx):
    if idx <0 or idx > len(my_list):
        return (None)
    idx_tmp = 0
    for element in my_list:
        if idx_tmp == idx:
            return (element)
        idx_tmp +=1
    
