#!/usr/bin/python3
def divisible_by_2(list=[]):
    my_list = list.copy()
    for i in range(len(my_list)):
        if list[i] % 2 == 0:
            my_list[i] = True
        else:
            my_list[i] = False
    return my_list
