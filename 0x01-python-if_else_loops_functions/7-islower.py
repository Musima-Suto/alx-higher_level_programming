#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    elif ord(c) not in range(97, 123):
        return False
