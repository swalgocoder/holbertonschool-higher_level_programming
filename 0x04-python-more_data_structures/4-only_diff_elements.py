#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_seen = []
    for i in set_1:
        if i not in set_2:
            c_seen.append(i)
    for j in set_2:
        if j not in set_1:
            c_seen.append(j)
    return c_seen
