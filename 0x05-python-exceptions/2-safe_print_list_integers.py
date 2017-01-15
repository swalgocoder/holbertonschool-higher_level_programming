#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i_cnt = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i_cnt += 1
            if i_cnt == x:
                break
        except(ValueError, TypeError):
            continue
    print("")
    return i_cnt
