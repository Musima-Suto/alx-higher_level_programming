#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv) - 1
    if number == 1:
        print("{} argument:".format(1))
    elif number == 0:
        print("{} arguments.".format(0))
    elif number > 1:
        print("{} arguments:".format(number))
    for i in range(1, number):
        print("{}:{}".format(i, sys.argv[i]))
