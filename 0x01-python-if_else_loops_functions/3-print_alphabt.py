#!/usr/bin/python3
def except_case():
    for char in range(ord('a'), ord('z') + 1):
        if char == ord('q') or char == ord('e'):
            continue
        else:
            print("{}".format(chr(char)), end='')


except_case()
