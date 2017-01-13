#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = []
    for i in my_list:
        if i not in seen:
            seen.append(i)
    return sum(seen)
