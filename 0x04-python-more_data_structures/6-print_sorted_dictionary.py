#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key, item in sorted(my_dict.items()):
        print ("{}:{}".format(key, item))
