#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = 0
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

