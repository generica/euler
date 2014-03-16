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

if __name__ == "__main__":

    tally = 0

    for num in xrange(0, 1000000):
        if ispalindrome(num) and ispalindrome(str(bin(num))[2:]):
            tally += num
            print tally
