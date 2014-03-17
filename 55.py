#!/usr/bin/python

import math

def ispalindrome(num):

    strnum = str(num)
    length = len(strnum)

    if length == 1:
        return True

    midpoint = int(math.floor(length / 2))

    start = strnum[:midpoint]
    end = strnum[-midpoint:]
    end_reversed = end[::-1]

    if end_reversed == start:
        return True
    else:
        return False

def islychrel(num):

    for i in range(0, 51):
        new = num + int(str(num)[::-1])
        if ispalindrome(new):
            return True
        num = new

    return False

if __name__ == "__main__":

    tally = 0
    no = 0

    for i in xrange(0, 10000):
        if islychrel(i):
            tally += 1
        else:
            no += 1

    print tally, no
