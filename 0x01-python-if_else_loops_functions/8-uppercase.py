#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            upper = ord(i) - 32
            str = str + chr(upper)
    print("{}".format(str))
