#!/usr/bin/python

import math

def ispalindrome(num):

    strnum = str(num)
    length = len(strnum)

    midpoint = int(math.floor(length / 2))

    start = strnum[:midpoint]
    end = strnum[-midpoint:]
    end_reversed = end[::-1]

    if end_reversed == start:
        return True
    else:
        return False


if __name__ == "__main__":

    largest = 0

    for x in range(100, 1000):
        for y in range(100, 1000):
            prod = x * y
            if ispalindrome(prod):
                if prod > largest:
                    largest = prod

    print largest
