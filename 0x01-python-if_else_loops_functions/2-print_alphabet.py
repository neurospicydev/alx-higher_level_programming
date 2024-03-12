#!/usr/bin/python3
def lower_case():
    for char in range(ord('a'), ord('z') + 1):
        print("{}".format(chr(char)), end='')


lower_case()
