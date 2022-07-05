#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = []
    arguments = len(sys.argv)
    for i in range(1, arguments):
        a.append(int(sys.argv[i]))
    total = sum(a)
    print(total)
