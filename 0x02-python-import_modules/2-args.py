#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len = len(sys.argv) - 1
    if len == 0:
        print("{:d} argument.".format(len))
    elif len == 1:
        print("{:d} argument:\n{:d}: {:s}".format(len, len, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len))
        for i in range(1, len + 1):
            print('{:d}: {:s}'.format(i, sys.argv[i]))
