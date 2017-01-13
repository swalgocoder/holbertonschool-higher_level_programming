#!/usr/bin/python
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    numerator = sum([v * w for v, w in my_list])
    denominator = sum([w for v, w in my_list])
    if (denominator != 0):
        return (float(numerator) / float(denominator))
    else:
        return 0
    
