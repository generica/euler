#!/usr/bin/python

import sys

def getnext(n):
    next = 0
    for digit in str(n):
        next += int(digit) ** 2
    if next == 1 or next == 89:
        return next
    else:
        return getnext(next)

if __name__ == "__main__":

    i = 0
    tally = 0

    while True:
        i += 1
        j = getnext(i)
        if j == 89:
            tally += 1

        if i % 100000 == 0:
            print i

        if i == 10000000:
            print tally
            sys.exit(0)
