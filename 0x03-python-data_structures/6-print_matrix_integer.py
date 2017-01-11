#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_row in matrix:
        for element in my_row:
            print("{:d}".format(element), end = '')
            if my_row.index(element) < len(my_row) - 1:
                print(' ',end = '')
        print('')
                
