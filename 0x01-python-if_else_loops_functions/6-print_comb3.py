#!/usr/bin/python3
def print_comb():
    for n in range(10):
        for m in range(n + 1, 10):
            if n < 8:
                print("{:d}{:d}, ".format(n, m), end="")
            else:
                print("{:d}{:d}".format(n, m), end=", " if m < 9 else "\n")


print_comb()
