#!/usr/bin/python3
def islower(c):
    if not c:
        raise valueError("Input is an empty string")
    if 'a' <= c <= 'z':
        return (True)
    else:
        return (False)
