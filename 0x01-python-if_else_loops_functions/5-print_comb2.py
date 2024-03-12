#!/usr/bin/python3
def print_nums():
    for n in range(100):
        if n < 99:
            print("{:02d}, ".format(n), end="")
        else:
            print("{:02d}".format(n))


print_nums()
