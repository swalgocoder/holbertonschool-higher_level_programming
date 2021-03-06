#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len = len(sys.argv)
    if len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
if sys.argv[2] in ['+']:
    print('{:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, add(a, b)))
if sys.argv[2] in ['-']:
    print('{:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, sub(a, b)))
if sys.argv[2] in ['*']:
    print('{:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, mul(a, b)))
if sys.argv[2] in ['/']:
    print('{:d} {} {:d} = {:d}'.format(a, sys.argv[2], b, div(a, b)))
