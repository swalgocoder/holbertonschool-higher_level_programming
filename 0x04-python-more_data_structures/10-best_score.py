#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict or my_dict == {}:
        return (None)
    biggest_val = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest_val:
            return (key)
