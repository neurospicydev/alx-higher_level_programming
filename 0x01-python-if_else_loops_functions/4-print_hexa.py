#!/usr/bin/python3
def print_hex():
    for num in range(99):
        print("{:d} = 0x{:x}".format(num, num))


print_hex()
