#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(0,x):
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except:
            break
    print("")
    return i
