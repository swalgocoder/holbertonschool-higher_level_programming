#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        np_print = 0
        for i in range (0,x):
            print("{}".format(my_list[i]), end = "")
            np_print += 1
        print("")
    except:
        # print("SomeError occurred")
        print("")
    return (np_print)
        
