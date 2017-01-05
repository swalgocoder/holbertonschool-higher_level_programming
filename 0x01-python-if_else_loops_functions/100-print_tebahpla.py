#!/usr/bin/python3
print("".join(['{}'.format(chr(n-32) if n % 2 else chr(n))
               for n in range(122, 96, -1)]), end="")
