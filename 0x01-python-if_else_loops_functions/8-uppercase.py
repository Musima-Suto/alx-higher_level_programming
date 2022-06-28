#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) in range(97, 123):
            upper = ord(i) - 32
            new_str = new_str + chr(upper)
        else:
            new_str = new_str + i
    print("{}".format(new_str))
