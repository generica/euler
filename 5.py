#!/usr/bin/python

import sys

if __name__ == "__main__":

    i = 0

    while True:
        i += 20
        if (i % 19 == 0) and (i % 18 == 0) and (i % 17 == 0) and (i % 16 == 0) and (i % 15 == 0) \
           and (i % 14 == 0) and (i % 13 == 0) and (i % 12 == 0) and (i % 11 == 0):
            print i
            sys.exit(0)
