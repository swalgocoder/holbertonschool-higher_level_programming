#!/usr/bin/python
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    numerator = 0
    denominator = 0

    for (v, w) in my_list:
        numerator += (v * w)
        denominator += w
        return numerator / denominator

    
