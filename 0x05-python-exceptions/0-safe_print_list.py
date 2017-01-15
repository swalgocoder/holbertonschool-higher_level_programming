#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nb_print = 0
    for nb_print in range(x):
        try:
            print('{}'.format(my_list[nb_print]), end = "")
            nb_print += 1
        except IndexError:
            print("")
            return (nb_print)
    print("")
    return (nb_print)
